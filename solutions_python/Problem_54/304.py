
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

c = int(raw_input())

for tc in xrange(c):
    ds = raw_input().split()
    n = int(ds[0])
    data = map(int, ds[1:])
    data.sort()
    T = data[1]-data[0]
    for i in xrange(1,n):
        T = gcd(T, data[i]-data[i-1])
    S = T - (data[0]%T)
    if S==T: S=0
    #print 'T:',T
    print 'Case #%d: %s' % (tc+1, str(S))
