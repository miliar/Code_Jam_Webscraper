import sys

def gcd(a,b):
    if b==0: return a
    return gcd(b, a%b)

def readints():
    x=sys.stdin.readline()
    x=x.split()
    l=len(x)
    for i in range(0,l):
        x[i]=int(x[i])
    return x


x=readints()
m = x[0]
for test in range(0,m):
    x=readints();
    n=x[0]
    d=abs(x[1] - x[2])
    for i in range(0,n):
        for j in range(i+1, n):
            d=gcd(d, abs(x[i+1]-x[j+1]))
    print "Case #%d: %d" % (test+1, (d - (x[1]%d))%d)
    sys.stderr.write('Case %d\n' % test)
