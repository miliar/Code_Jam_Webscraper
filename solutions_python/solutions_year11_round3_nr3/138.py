import sys

def ReadInts():
    return list(map(int, sys.stdin.readline().strip().split()))

def GCD(a,b):
    while b>0:
        a = a%b
        a,b = b,a

    return a

def LCD(a,b):
    return a * b / GCD(a,b)

T = ReadInts()[0]
for tc in xrange(1,T+1):
    N,L,H = ReadInts()
    F = ReadInts()

    r = -1
    for n in xrange(L,H+1):
        cnt = 0
        for x in F:
            if n%x==0 or x%n==0:
                cnt = cnt + 1

        if cnt == len(F):
            r = n
            break

    if r<0:
        print "Case #%d: NO" % tc
    else:
        print "Case #%d: %d" % (tc, r)
