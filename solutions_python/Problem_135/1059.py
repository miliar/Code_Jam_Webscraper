#!/usr/bin/python
#encoding:UTF-8
import linecache
filename='A--small-attempt7.in'
cn=int(linecache.getline(filename,1))

l=2
n=2

for i in range(cn):
	a=linecache.getline(filename,l+i*10+int(linecache.getline(filename,l+i*10))).strip('\n').split(' ')
	b=linecache.getline(filename,l+5+i*10+int(linecache.getline(filename,l+5+i*10))).strip('\n').split(' ')
	ss=i+1
	c=[i for i in a if i in b]
	if len(c)==1:
		print "Case #%s: %s" %(ss,c[0])
	elif len(c) >=2:
		print "Case #%s: Bad magician!" %ss
	elif len(c) <=0 :
		print "Case #%s: Volunteer cheated!" %ss
	
