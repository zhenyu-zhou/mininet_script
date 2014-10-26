#!/usr/bin/python

from mininet.topo import Topo
from mininet.node import Host, OVSSwitch, Controller
from mininet.link import Link

h1 = Host('h1')
h2 = Host('h2')
s1 = OVSSwitch('s1', inNamespace=False)
c0 = Controller('c0', inNamespace=False)
Link(h1,s1)
Link(h2,s1)
h1.setIP('10.1/8')
h2.setIP('10.2/8')
c0.start()
s1.start([c0])
print h1.cmd('ping -c1', h2.IP())
s1.stop()
c0.stop()
