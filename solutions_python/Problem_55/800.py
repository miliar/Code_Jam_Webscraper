from numpy import *
f = open('C-small-attempt0.in', 'r')
d = open('c.out', 'w')
c=int(f.readline())
for test in range(1,c+1):
	buffer=0
	moola=0
	controll=f.readline()
	groups=f.readline()
	controll=controll.split()
	controll=map(int, controll) 
	groups=groups.split()
	queu=map(int, groups) 
	seat=list()
	temp=0
	for i in range(1,controll[0]+1):
		buffer=0
		while queu and queu[0]+buffer <= controll[1]:
			buffer+=queu[0]
			temp=queu.pop(0)
			seat.append(temp)
		for x in seat:
			queu.append(x)	
		seat=[]
		moola+=buffer
	d.write ('Case #{0}: {1}\n'.format(test,moola))
