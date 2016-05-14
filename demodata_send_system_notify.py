#!/usr/bin/env python

# import syspath
from lib.configloader import ConfigLoader
import demodata
import lib.upstream

_config = ConfigLoader("config")

# Demodata
notify_sys = demodata.notify_sys

print("Sending to server (notify " + notify_sys.name + ")...")
response = lib.upstream.pushSystemNotify(_config, notify_sys.urn, notify_sys)
print("Response:\n" + response)
