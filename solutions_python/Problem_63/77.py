import math


f = [l[:-1] for l in file("in")]
f = f[1:]
case=0
for l in f:
    case+=1
    L, P, C = [int(x) for x in l.split(" ")]
    
    times=0
    #keep taking geom means until you get where you wanna be.

    #point of contention - round up? down? all around?
    new = P
    while new>L*C:
        new =  (new*L) ** (1/float(2))
        times+=1

    print "Case #%d: %d" % (case, times)
