#!/usr/bin/python
#encoding:UTF-8
import linecache,types,sys
filename=sys.argv[1]
cn=int(linecache.getline(filename,1))

l=2
n=2

for i in range(cn):
	a=linecache.getline(filename,l+i).strip('\n').split(' ')
	aa=[float(j) for j in a]
	c,f,x=aa
	j=0
	time=0;
	while x/(2+j*f)>(c/(2+j*f)+x/(2+(j+1)*f)):
		time=time+c/(2+j*f)
		j=j+1
	time=time+x/(2+j*f)
	time = float('%0.7f'%time) 
	print "Case #%s: %s" %(i+1,time)
