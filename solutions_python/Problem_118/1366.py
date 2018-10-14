import cStringIO
from sys import stdin

def isPali(a):
    a = str(a)
    n = len(a)
    if n == 1:
        return True
    m = n/2
    return a[:m] == a[-1:-m-1:-1]

def nextPali(a):
    if isPali(a):
        return int(a)
    a = str(a)
    n = len(a)
    m = n/2
    odd = n%2
    flp = int(a[:m+odd])
    lp = list(a[:m])
    rp = int(a[-m:])
    lp.reverse()
    lp = int(''.join(lp))
    if rp < lp:
        rp = lp
        return int(str(flp) + str(rp))
    else:
        return nextPali(str(flp+1) + '0'*m)

T = int(raw_input())
all = cStringIO.StringIO(stdin.read())

for t in xrange(T):
    A, B = map(int, all.next().split())
    C = 0
    a = int(A**0.5)
    b = int(B**0.5)

    pali = nextPali(a)
    while pali <= b:
        palipali = pali**2
        if palipali>=A and isPali(palipali):
            C += 1
        pali = nextPali(pali+1)
    print 'Case #'+ str(t+1) +': ' + str(C)
