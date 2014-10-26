#!/usr/bin/python

from mininet.topo import Topo
from mininet.node import Host, OVSSwitch, Controller
from mininet.link import Link
from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.cli import CLI

net = Mininet(SingleSwitchTopo(2))
net.start()
print "Start!"
CLI(net)
net.stop()

