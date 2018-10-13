import sys

def ReadInts():
    return map(int, sys.stdin.readline().strip().split())

def comp(x,y):
    if x[2]==y[2]:
        if x[1]==y[1]:
            return y[0]-x[0]
        return y[1]-x[1]
    return y[2] - x[2]

T = ReadInts()[0]
for cs in xrange(1,T+1):
    ints = ReadInts()
    N = ints[0]
    S = ints[1]
    p = ints[2]
    totals = ints[3:]
    
    googlers = []
    for total in totals:
        n = total/3
        r = total%3

        l = [n,n,n]
        if r>0:
            l[2] += 1
            r -= 1
        if r>0:
            l[1] += 1
            r -= 1

        googlers.append(l)

    googlers.sort(comp)

    res = 0
    for g in googlers:
        if g[2]>=p:
            res += 1
        else:
            if S>0:
                g[2] += 1
                g[1] -= 1
                if g[1]<0 or g[2]>10 or g[2]-g[0]>2:
                    g[2] -= 1
                    g[1] += 1
                    continue
                S -= 1
                if g[2] >= p:
                    res += 1

    #print googlers
    print 'Case #%d: %d' % (cs, res)
