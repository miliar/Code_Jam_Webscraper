
def _add(a,b):
    return a ^ b

import sys

f = open(sys.argv[1])

t=int(f.readline().rstrip())

for i in range(1,t+1):
    n=int(f.readline())
    cs = [int(s) for s in f.readline().strip().split(" ")]

    #print n,cs
    
    maxt1=0
    
    for imask in range(0,2**n):
        #print 'imask',imask
        f1=0
        t1=0
        f2=0
        t2=0
        
        for ni in range(0,n):
            #print imask & 2**ni
            if imask & 2**ni:
                t1 = t1 + cs[ni]
                f1 = _add(f1,cs[ni])
            else:
                t2 = t2 + cs[ni]
                f2 = _add(f2,cs[ni])
        
        #print t1,t2
        #print f1,f2
        
        if f1>0 and f1 == f2 and t1>maxt1:
            maxt1 = t1
    print 'Case #%d: %s'%(i,maxt1 > 0 and maxt1 or 'NO')
    
f.close()
