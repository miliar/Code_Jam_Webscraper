#!/usr/bin/python

l=["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"]
m=["our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"]


d={}
mainlen=len(l)
for i in range(mainlen):
	lent=len(l[i])
	for j in range(lent):
		if l[i][j] not in d:
			d[l[i][j]]=m[i][j]

d['q']='z'
d['z']='q'
#print len(d)
#new_d=sorted(d.values())
#print new_d
#new_d=sorted(d.keys())
#print new_d

a=input()
for i in range(a):
	s=raw_input()
	new_s=""
	print "Case #"+str(i+1)+":",
	for let in s:
		new_s=new_s+d[let]
	print new_s
