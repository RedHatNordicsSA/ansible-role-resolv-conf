ansible-role-resolv-conf
=========================

Creates default resolv.conf name resolution settings for VM to reach DNS servers.

Requirements
------------

No requirements.


Role Variables
--------------

There is list of variables in defaults/main.yml which can be overridden in
vault or in Tower. You may need to modify them to use this role.

Dependencies
------------

No dependencies.

Example Playbook
----------------

  - include_role:
      name: ansible-role-resolv-conf

License
-------

BSD

Author Information
------------------

Peter Gustafsson pgustafs@redhat.com
[Red Hat](https://redhatnordicssa.github.io/)
