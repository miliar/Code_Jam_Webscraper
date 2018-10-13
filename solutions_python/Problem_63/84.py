import sys
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
    L, P, C = readlinearray(int)
    
    k = 0
    n = L
    while n < P:
        k += 1
        n *= C
    
    res = 0
    n = 1
    while n < k:
        res += 1
        n *= 2
    
    print 'Case #' + str(test+1) + ': ' + str(res)
