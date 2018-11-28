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
    N, M = readlinearray(int)
    
    res = 0
    L = []
    for i in range(N):
        ss = raw_input().split('/')
        acc = '/'
        for s in ss[1:]:
            acc += s
            L.append(acc)
            acc += '/'
    
    for i in range(M):
        ss = raw_input().split('/')
        acc = '/'
        for s in ss[1:]:
            acc += s
            if not acc in L:
                res += 1
                L.append(acc)
            acc += '/'
    
    
    print 'Case #' + str(test+1) + ': ' + str(res)
