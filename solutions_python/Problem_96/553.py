def solve():
    a = map(int,raw_input().split())
    n,s,p = a[:3]
    t = a[3:]
    v = 3 * p - 2
    a = sum(1 for x in t if x >= v)
    b = sum(1 for x in t if max(2, v-2) <= x < v)
    #print a,b,t,v
    return a + min(b, s)

t = input()
for i in xrange(t):
    print "Case #%d: %d"%(i+1,solve())
