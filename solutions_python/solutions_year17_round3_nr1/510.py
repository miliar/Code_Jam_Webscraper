import math
t = int(raw_input())
pi =math.pi
for c in xrange(1, t + 1):
    # intitalization here
    y = 0
    n, k = [int(s) for s in raw_input().split(" ")]
    ar = [(0,0)] * n
    for i in xrange(0, n):
        ar[i] = [int(s) for s in raw_input().split(" ")]
        # r,h
        #print r,h
    #print ar
    maxy = 0
    for j in xrange(0, n):
        arx = ar[:]
        baseCylender = arx[j]
        del arx[j]
        arx= sorted(arx, key=lambda x:x[0]* x[1], reverse = True)
        chosen= arx[:(k-1)]

        y = baseCylender[0]*baseCylender[0]* pi +  baseCylender[1]*baseCylender[0]*2*pi    + sum([t[0]*t[1]*2*pi for t in chosen])
        #print chosen, y, baseCylender[0]*baseCylender[0]* pi
        if y > maxy :
            maxy = y
    print "Case #{}: {:f}".format(c, maxy)
