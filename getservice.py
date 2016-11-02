#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: getservice
version_added: "2.1"
short_description: Get Linux/Unix Service List
description:
   - List the Services present on a Linux/Unix node
options: {}
author:
    - "Lal Krishna"
'''

EXAMPLES = '''
# List the services
	getservice:
'''

import time
import sys
import os

from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(required=False, default=None),
        ),
                supports_check_mode=True
    )
    checkresp = module.run_command('service --status-all')
    module.exit_json(changed=False, msg='Services are {}'.format(checkresp[1]))

if __name__ == '__main__':
    main()