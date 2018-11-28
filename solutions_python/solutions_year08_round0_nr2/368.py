#!/usr/bin/python
import sys
import string
import pdb

def str2min(x):
	hr,min=x.split(':')
	hr=int(hr)
	min=int(min)
	totalmin=60*hr+min
	return totalmin


archivo=sys.argv[1]
fd=open(archivo)
Ncases=int(fd.readline())
for j in range(Ncases):
	T=int(fd.readline())
	NA,NB=fd.readline().split()
	NA=int(NA)
	NB=int(NB)
	sch=[]
	for i in range(NA):
		hor=fd.readline().split()
		hor[0]=str2min(hor[0])
		hor[1]=str2min(hor[1])
		hor.append(0)
		sch.append(hor)
	for i in range(NB):
		hor=fd.readline().split()
		hor[0]=str2min(hor[0])
		hor[1]=str2min(hor[1])
		hor.append(1)
		sch.append(hor)
	sch.sort()
	viajes=[0,0]
	while sch!=[]:
		tren=[sch[0][1]+T,sch[0][2]]
		viajes[tren[1]]=viajes[tren[1]]+1
		sch.pop(0)
		borrar=[]
		for tt in sch:
			if tren[0]<=tt[0] and tren[1]^tt[2]:
				tren=[tt[1]+T,tt[2]]
				borrar.append(tt)
		for br in borrar:
			sch.remove(br)
	print "Case #"+str(j+1)+": "+str(viajes[0])+" "+str(viajes[1])
