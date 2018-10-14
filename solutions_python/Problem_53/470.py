#!/usr/bin/python
import os
for fn in os.listdir('.'):
	if fn.rfind("in")!=-1:
		fnn=fn
		break
print "reading file",fnn
f=open(fnn,"r")
fw=open(fnn+".out",'w')
line=f.readline().split()
L=int(line[0])
for i in range(L):
	line=f.readline().split()
	N = int(line[0])
	K = int(line[1])
	#print "n,k = ",N,",",K,":",
	fw.write("Case #"+str(i+1)+": ")
	if (K+1)% int(pow(2,N))==0:
		fw.write("ON\n")
		#print "ON"
	else:
		fw.write("OFF\n")
		#print "OFF"
f.close()
fw.close()
print "done"