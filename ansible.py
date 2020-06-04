from config import *
from schema import *
from flask import jsonify

@app.route("/ansible/list")
def ansible_list():
  ansible_groups=dict()

  for role in Role.query.all():
    ansible_group=dict()
    ansible_group["hosts"]=[]
    for host in Host.query.filter(Host.role_id==role.id):
      ansible_group["hosts"].append(host.name)
    ansible_group["vars"]={"doi_role":role.name}
    ansible_group["children"]=[]
    ansible_groups[role.name]=ansible_group
  for group in Group.query.all():
    ansible_group=dict()
    ansible_group["hosts"]=[]
    for host in Host.query.filter(Host.group_id==group.id):
      ansible_group["hosts"].append(host.name)
    ansible_group["vars"]={"doi_group":group.name}
    ansible_group["children"]=[]
    ansible_groups[group.name]=ansible_group
  for system in System.query.all():
    ansible_group=dict()
    ansible_group["hosts"]=[]
    for host in Host.query.filter(Host.system_id==system.id):
      ansible_group["hosts"].append(host.name)
    ansible_group["vars"]={"doi_system":system.name}
    ansible_group["children"]=[]
    ansible_groups[system.name]=ansible_group
  return jsonify(ansible_groups)

@app.route("/ansible/host/<hostname>")
def ansible_host(hostname):
  ansible_vars = dict()
  host = Host.query.filter(Host.name==hostname).first()
  if not host:
    abort(404)
  if host.ansible_vars:
    for ansible_var in host.ansible_vars.split(" "):
      if len(ansible_var.split("="))==2: # yes, this is weak but I'm not gonna use yaml/json in frontend to store key-value pairs... or maybe I am but not right now
        ansible_vars[ansible_var.split("=")[0]]=ansible_var.split("=")[1]
      else:
        ansible_vars[ansible_var]=None
  return jsonify(ansible_vars)
