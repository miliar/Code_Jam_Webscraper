import sys
import fractions

def dbg(a): sys.stderr.write(str(a))

def alloc(size, default = 0): return [default] * size
def alloc2(r, c, default = 0): return [alloc(c, default)] * r
def isset(a, bit): return ((a >> bit) & 1) > 0
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo): return [foo() for i in xrange(N)]
def readlinearray(foo): return map(foo, raw_input().split())
def dig(c): return ord(c) - 48

T = readint()

for test in xrange(T):
    L = raw_input().split()
    N = int(L[0])
    t = map(long,L[1:])
    
    k = abs(t[1] - t[0])
    for i in range(len(t)):
        for j in range(i):
            k = fractions.gcd(k, abs(t[i] - t[j]))

    y = k - (t[0]%k)
    if t[0]%k == 0: y = 0
     
    print "Case #%d: %d" % (test+1, y)
