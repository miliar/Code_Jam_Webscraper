import sys

def gcd(a,b):
    while b > 0: a,b = b, a%b
    return a

cases=int(sys.stdin.readline())

for j in range(1, cases+1):
    [length, data]=sys.stdin.readline().split(' ', 1)
    data=map(int, data.split())
    data=sorted(data)
    d=[]
    for i in range(1, len(data)):
        d.append(data[i]-data[i-1])
    g=d[0]
    for i in range(1, len(d)):
        g=gcd(g, d[i])
    print "Case #%d: %d"%(j, (g-min(data)%g)%g)
