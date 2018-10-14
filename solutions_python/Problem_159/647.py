# -*- coding: utf-8 -*-
import sys

f_in = sys.argv[1]
f_out = sys.argv[2]

testcases=[]

with open(f_in) as f:
    T = int(f.readline())
    for t in range(T):
	f.readline()
	testcases.append(f.readline())

for k,t in enumerate(testcases):
    t=t.strip().split(' ')
    t=[int(s) for s in t]

    method1=0
    method2=0
    diffs=[0]
    incr=0
    decr=0
    for i in range(1,len(t)):
	diffs.append(t[i-1]-t[i])
	if t[i]<t[i-1]:
	    method1=method1+t[i-1]-t[i]
    
    md = max(diffs)
    print diffs, md
    if md>0:
	for i in range(len(t)-1):
	    if t[i+1] != 0:
		if t[i+1]>t[i]:
		    method2 = method2 + min(t[i],md)
		else:
		    if t[i]<md:
			method2=method2+t[i]
		    else:
			method2 = method2 + md
	    else:
		method2=method2+t[i]
    





    with open(f_out,'a') as g:
	g.write('Case #'+str(k+1)+': '+str(method1)+' '+str(method2)+'\n')
    print 'Case #'+str(k+1)+': '+str(method1)+' '+str(method2)
#    print t

