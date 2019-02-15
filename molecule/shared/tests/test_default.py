import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_resolv_file(host):
    f = host.file("/etc/resolv.conf")
    assert f.contains("search infra.example.com example.com")
