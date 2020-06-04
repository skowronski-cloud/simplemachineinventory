# SimpleMachineInventory

## deploy

### prerequisites
* Linux
* python3.7
* some reverse proxy for covering up auth and access control
* `pip3 install -r requyirements.txt`


## usage 
### managing hosts and disks

via web-gui at `/SimpleMachineInventory/`

to write changes you must auth using "login" button and be listed in db as writer

### managing locations, roles, groups, systems and accessing data programatically

via API at `/SimpleMachineInventory/api/` - there's swagger or you can use postman

### accessing ansible inventory

via `/SimpleMachineInventory/ansible/list` and `/SimpleMachineInventory/ansible/host/<hostname>` - see https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory-scripts
