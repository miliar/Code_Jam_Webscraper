import sys
import time
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def dig(c): return ord(c) - 48

t00 = time.clock()
        
def solve():
    P = readint()
    Mlist = readarray(int)
    for p in xrange(P):
        dummy = readarray(int)

    ans = 0
    path = []
    for p in xrange(P+1):
        indexes = []
        for i,m in enumerate(Mlist):
            if m == p: indexes.append(i)
        for i in indexes:
            j = (i+2**P)//2
            pi = []
            while j > 0:
                pi.append(j)
                j //= 2
            c = 0
            for q in pi:
                if q in path: c += 1
                else: path.append(q)
            ans += max(P-p-c,0)
    return ans

for t in range(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    ans = solve()
    
    print "Case #%d: %d" % (t+1,ans)
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
