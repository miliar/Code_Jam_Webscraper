from string import *
from math import *
def isPalin(x):
    strx = str(x)
    for i in range(len(strx)):
        if strx[i]!=strx[len(strx)-i-1]:
            return False
    #print "true:",strx
    return True
T = input()
f = file('out.txt', 'w')
for Ti in range(1,T+1):
    inp = raw_input().strip().split()
    A = atoi(inp[0])
    B = atoi(inp[1])
    sqa = int(ceil(sqrt(A)))
    sqb = int(floor(sqrt(B)))
    #print sqa,sqb
    out=0
    for i in range(sqa,sqb+1):
        if isPalin(i) and isPalin(i*i):
            out+=1
    f.write("Case #"+str(Ti)+": "+str(out)+"\n")
f.close()
