#!/usr/bin/python
import os
from collections import deque
for fn in os.listdir('.'):
	if fn.rfind("in")!=-1:
		fnn=fn
		break
print "reading file",fnn
f=open(fnn,"r")
fw=open(fnn+".out",'w')
line=f.readline().split()
T=int(line[0])
for i in range(T):
	line=f.readline().split()
	R = int(line[0])
	k = int(line[1])
	N = int(line[2])
	line=f.readline().split()
	G=deque()
	V=deque()
	for c in line:
		G.append(int(c))
	fw.write("Case #"+str(i+1)+": ")
	suma=0
	for go in range(R):
		s = 0
		while len(G)>0 and G[0]+s <=k:
			s+=G[0]
			suma+=G[0]
			V.append(G.popleft())
		while len(V)>0:
			G.append(V.popleft())
	fw.write(str(suma)+"\n")
f.close()
fw.close()
print "done"