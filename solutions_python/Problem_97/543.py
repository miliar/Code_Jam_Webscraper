d = {}
k = 0
p = 10
for i in xrange(12,2000001):
    while p * 10 <= i: p *= 10
    while i < p or i not in d:
        if i >= p: d[i] = k
        i = (i%p)*10 + i/p
    k += 1

def solve():
    a,b = map(int,raw_input().split())
    r = {}
    for i in xrange(a,b+1):
        if i in d:
            r[d[i]] = r.get(d[i],0) + 1
#    for k,v in r.iteritems():
#        if v<2: continue
#        print v,
#        for x,y in d.iteritems():
#            if y!=k: continue
#            if a <= x <= b: print x,
#        print
    return sum(x*(x-1) / 2 for x in r.itervalues())

t = input()
for i in xrange(t):
    print "Case #%d: %s"%(i+1,solve())
