import os
import math
import copy
import sys

os.chdir('/Users/Dana/Downloads/A')
f = open('A-small-attempt0.in','r')
fo = open('A.out','w')
T = int(f.readline())
for ite in range(T):
    a,b = str.split(f.readline())
    smax = int(a)
    shy = [int(x) for x in list(b)]
    shy = [sum(shy[:i+1]) for i in range(smax+1)]
    #print(shy)
    if (smax==0):
        res = 0
    else:
        res = max([i+1-shy[i] for i in range(smax)])
    if (res<0):
        res = 0
    #print(res)
    #print(n)
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    fo.write(str(res))
    fo.write('\n')
fo.close()

