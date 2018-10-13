# -*- coding: utf-8 -*-
import sys

f_in = sys.argv[1]
f_out = sys.argv[2]

testcases=[]

with open(f_in) as f:
    T = int(f.readline())
    for t in range(T):
	testcases.append(f.readline())

for k,t in enumerate(testcases):
    t=t.strip().split(' ')
    Smax=int(t[0])
    t=t[1]

    people = int(t[0])
    add = 0
    for i in range(1,len(t)):
	if i > people and int(t[i])>0:
#	    print 'people:',people, ' vs ', 'i: ', i, ', t[i]', t[i]
	    add = add + (i-people)
	    people = people + (i-people)+ int(t[i])

	else:
	    people = people + int(t[i])
    with open(f_out,'a') as g:
	g.write('Case #'+str(k+1)+': '+str(add)+'\n')
    #print 'Case #'+str(k+1)+': '+str(add)
#    print t

