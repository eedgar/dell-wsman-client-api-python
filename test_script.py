#!/usr/bin/env python
from wsman import WSMan
from wsman.provider.remote import Remote
from wsman.transport.twisted import Twisted

from wsman.format.command import OutputFormatter
from wsman.loghandlers.HTMLHandler import HTMLHandler 

import pdb;pdb.set_trace()
wsman = WSMan(transport=Twisted())

remote = Remote("172.26.4.55", 'root', 'rootpw')
refs = wsman.enumerate_keys("DCIM_NICView", "root/dcim", remote=remote)
   
# Find the reference we want a full GET on
for reference in refs:
    if reference.get("InstanceID")[0] == "NIC.Slot.2-2-4":
        break
   
my_nic = wsman.get(reference, "", remote=remote)
for key in my_nic.keys:
     print key, ":", my_nic.get(key)
