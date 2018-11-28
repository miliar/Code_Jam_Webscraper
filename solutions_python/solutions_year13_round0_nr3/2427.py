import sys
from math import sqrt,ceil,floor



def pal(x):
    x = str(x)
    return x==x[::-1]

f = open('C.in')
f = sys.stdin
for PROB in xrange(int(f.readline())):
    fs = []
    m,M = map(int,f.readline().split())
    mm,MM = int(ceil(sqrt(m))),int(floor(sqrt(M)))
    for i in range(mm,MM+1):
        if pal(i):
            if pal(i**2): fs.append(i**2)
            #if pal(sqrt(i)): fs.append(sqrt(i))
    print "Case #%s: %s"%(PROB+1,len(fs))

    
        
        
    

