import sys
def gcd(a,b):
    if a==0: return b
    if b==0: return a
    s = 0
    while (a|b)&1 == 0:
        s += 1
        a>>=1
        b>>=1
    aa = a
    while a&1 == 0:
        a>>=1
    t = True
    while b != 0 or t:
        t = False
        while b&1==0:
            b>>=1
        if a<b:
            b-=a
        else:
            d = a-b
            a=b
            b=d
        b>>=1
    return a<<s

def run(N, K):
    D = []
    for i in range(N-1):
        D.append(abs(K[i]-K[i+1]))


    for i in range(len(D)-1):
        D[i+1] = gcd(D[i],D[i+1])
    gd = D[N-2]
    mn = min(K)
    q = (mn-1)/gd + 1
    return q*gd-mn
         

f = open(sys.argv[1])

for i,l in enumerate(f.readlines()):
    if i > 0 and len(l) > 1:
        N = l.split(' ')[0]
        N = int(N)
        K = [int(k) for k in l.split(' ')[1:]]
        r = run(N,K)
        print 'Case #%s: %s' % (i,r)
