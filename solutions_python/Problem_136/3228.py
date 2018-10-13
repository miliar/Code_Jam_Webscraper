import sys

def resolve(c,f,x):
    #print c,f,x
    r = x/2.0
    r0 = r
    cache = {}
    prod = 2.0
    farms = 1
    while(True):
        #print "r =",r
        #print cache
        #print "farms = ", farms
        t = 0.0
        if farms in cache:
            #print farms
            t += cache[farms]
            prod = prod + f
            farms += 1
            t += x/prod
            if t < r:
                r = t
            elif t > cache[farms-1]:
                break
        else:
            if farms == 1:
                cache[1] = c / prod
            else:
                cache[farms] = cache[farms -1] + c / prod
    #print cache
    return r


inpu = open(sys.argv[1])
cases = inpu.readline()[:-1]
for i in xrange(int(cases)):
    l = inpu.readline()[:-1].split(" ")
    c = float(l[0])
    f = float(l[1])
    x = float(l[2])
    print("Case #%i: %f" %(i+1, resolve(c,f,x)))

