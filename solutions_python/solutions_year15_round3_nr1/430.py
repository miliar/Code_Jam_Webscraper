# -*- coding: utf-8 -*-
import sys

def solve(test):
    r=test[0]
    c=test[1]
    w=test[2]
    if w==1:
	ntrap=r*c-1
    elif c%w==0:
	ntrap=r*(c/w-1)
    else:
	ntrap=r*c/w
    return ntrap + w


f_in = sys.argv[1]
f_out = sys.argv[2]

testcases=[]

with open(f_in) as f:
    T = int(f.readline())
    for t in range(T):
	testcases.append(f.readline())

ans=[]
for test in testcases:
    test=map(int,test.split(' '))
    ans.append(solve(test))

with open(f_out,'w') as g:
    for k,a in enumerate(ans):
	g.write('Case #'+str(k+1)+': '+str(a)+'\n')

