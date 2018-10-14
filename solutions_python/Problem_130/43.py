N = 0
def f(x):
    res=0
    while 2**res <= x:
        res+=1
    return res-1
def could(x, h):
    global N
    maks = f(2**N-x)
    return (2**(N-maks) <= h+1)
def must(x, h):
    global N
    maks = f(x+1)
    return (2**N - 2**(N-maks) + 1 <= h+1)
T = input()
for t in range(T):
    N, p = (int(x) for x in raw_input().split())
    p-=1
    s=0
    e=2**N-1
    while s<e:
        a=(s+e+1)/2
        if could(a,p): s=a
        else: e=a-1
    c = s
    s=0
    e=2**N-1
    while s<e:
        a=(s+e+1)/2
        if must(a,p): s=a
        else: e=a-1
    m = s
    print 'Case #{0}: {1} {2}'.format(t+1, m, c)
