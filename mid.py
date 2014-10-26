#/usr/bin/python

import sys
import time

from mininet.topo import Topo
from mininet.node import Host, OVSSwitch, Controller, RemoteController
from mininet.link import Link
from mininet.net import Mininet
from mininet.cli import CLI

f_flow=open('flows', 'w')
#f_tcp=open('tcpdump', 'w')
f_arp=open('arp', 'w')

net = Mininet()
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
s1 = net.addSwitch('s1', listenPort=6634)
net.addController('c0', controller=RemoteController, ip='192.168.56.1')
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s1)
net.start()

h1.setMAC('00:00:00:00:00:01')
h2.setMAC('00:00:00:00:00:01')
h3.setMAC('00:00:00:00:00:03')

#print "aa"
#f_tcp.write(s1.cmd('tcpdump -w log.pcap &'))
s1.cmd('tcpdump -w log.pcap &')
#print "bb"

for i in range(1, 3):	
	print i
	f_flow.write(str(i)+'\n')
	f_arp.write(str(i)+'\n')
	f_arp.write('h1\n'+h1.cmd('arp -n'))
	f_arp.write('h2\n'+h2.cmd('arp -n'))
	f_arp.write('h3\n'+h3.cmd('arp -n'))
	f_arp.write('---------\n')
	h1.cmd('arp -d', h2.IP())
	h1.cmd('arp -d', h3.IP())
	h1.cmd('arping -c1', h3.IP())
	#time.sleep(5)
	print "---------"
	print s1.cmd('dpctl dump-flows tcp:localhost:6634')
	f_flow.write("---------\n")
	f_flow.write(s1.cmd('dpctl dump-flows tcp:localhost:6634')+'\n')
	f_arp.write('h1\n'+h1.cmd('arp -n'))
        f_arp.write('h2\n'+h2.cmd('arp -n'))
        f_arp.write('h3\n'+h3.cmd('arp -n'))
        f_arp.write('---------\n')
	h2.cmd('arp -d', h1.IP())
	h2.cmd('arp -d', h3.IP())
	h2.cmd('arping -c1', h3.IP())
	print "---------"
        print s1.cmd('dpctl dump-flows tcp:localhost:6634')
	f_flow.write("---------\n")
	f_flow.write(s1.cmd('dpctl dump-flows tcp:localhost:6634')+'\n')
	f_arp.write('h1\n'+h1.cmd('arp -n'))
        f_arp.write('h2\n'+h2.cmd('arp -n'))
        f_arp.write('h3\n'+h3.cmd('arp -n'))
        f_arp.write('---------\n')
	print "---------"
	f_flow.write("---------\n")

CLI(net)
net.stop()

