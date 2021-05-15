from config import *
from safrs import SAFRSBase

class User(SAFRSBase, db.Model):
  __tablename__ = "User"
  id          = db.Column(db.Integer, primary_key=True)
  upn         = db.Column(db.String(64))
class Location(SAFRSBase, db.Model):
  __tablename__ = "Location"
  id          = db.Column(db.Integer, primary_key=True)
  datacenter  = db.Column(db.String(64))
  hypervisor  = db.Column(db.String(64))
  hosts       = db.relationship("Host", back_populates="location")
class Species(SAFRSBase, db.Model):
  __tablename__ = "Species"
  id          = db.Column(db.Integer, primary_key=True)
  name        = db.Column(db.String(64))
  hosts       = db.relationship("Host", back_populates="species")
class Role(SAFRSBase, db.Model):
  __tablename__ = "Role"
  id          = db.Column(db.Integer, primary_key=True)
  name        = db.Column(db.String(64))
  notes       = db.Column(db.String(1024))
  hosts       = db.relationship("Host", back_populates="role")
class Group(SAFRSBase, db.Model):
  __tablename__ = "Group"
  id          = db.Column(db.Integer, primary_key=True)
  name        = db.Column(db.String(64))
  color       = db.Column(db.String(64))
  owners      = db.Column(db.String(1024))
  notes       = db.Column(db.String(1024))
  members     = db.relationship("HostGroupMemebership", back_populates="group", lazy="select")
class HostGroupMemebership(SAFRSBase, db.Model):
  __tablename__ = "HostGroupMemebership"
  id          = db.Column(db.Integer, primary_key=True)
  host_id     = db.Column(db.Integer, db.ForeignKey("Host.id"))
  host        = db.relationship("Host", back_populates="memberships")
  group_id    = db.Column(db.Integer, db.ForeignKey("Group.id"))
  group       = db.relationship("Group", back_populates="members")
class System(SAFRSBase, db.Model):
  __tablename__ = "System"
  id          = db.Column(db.Integer, primary_key=True)
  name        = db.Column(db.String(64))
  icon        = db.Column(db.String(1024))
  hosts       = db.relationship("Host", back_populates="system")
class Disk(SAFRSBase, db.Model):
  __tablename__ = "Disk"
  id          = db.Column(db.Integer, primary_key=True)
  host_id     = db.Column(db.Integer, db.ForeignKey("Host.id"))
  host        = db.relationship("Host", back_populates="disks")
  size        = db.Column(db.Integer())
  name        = db.Column(db.String(64))
  notes       = db.Column(db.String(1024))
class Host(SAFRSBase, db.Model):
  __tablename__ = "Host"
  id          = db.Column(db.Integer, primary_key=True)
  ip          = db.Column(db.String(64))
  name        = db.Column(db.String(64))
  location_id = db.Column(db.Integer, db.ForeignKey("Location.id"), default=999999)
  location    = db.relationship("Location", back_populates="hosts")
  species_id  = db.Column(db.Integer, db.ForeignKey("Species.id"), default=999999)
  species     = db.relationship("Species",  back_populates="hosts")
  role_id     = db.Column(db.Integer, db.ForeignKey("Role.id"), default=999999)
  role        = db.relationship("Role", back_populates="hosts")
  purpose     = db.Column(db.String(1024))
  cpu         = db.Column(db.Integer(), default=0)
  ram         = db.Column(db.Integer(), default=0)
  disks       = db.relationship("Disk", back_populates="host", lazy="select")
  memberships = db.relationship("HostGroupMemebership", back_populates="host", lazy="select")
  system_id   = db.Column(db.Integer, db.ForeignKey("System.id"), default=999999)
  system      = db.relationship("System", back_populates="hosts")
  notes       = db.Column(db.String(1024))
  ansible_vars= db.Column(db.String(4096))
  protections = db.Column(db.String(1024))