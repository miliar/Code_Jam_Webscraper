import sys
import time
import re
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def dig(c): return ord(c) - 48

t00 = time.clock()


        
def solve(N,M,ndirs,mdirs):
    nlist = []
    for n in ndirs:
        a = n[1:].split('/')
        l = len(a)
        for i in xrange(1,l+1):
            nlist.append('/'.join(a[:i]))
    nlist2 = list(set(nlist))
    mlist = []
    for m in mdirs:
        a = m[1:].split('/')
        l = len(a)
        for i in xrange(1,l+1):
            mlist.append('/'.join(a[:i]))
    mlist2 = list(set(mlist))
    res = 0
    for m in mlist2:
        if not m in nlist2: res += 1
    
    return res

    

for t in range(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    N,M = readarray(int)
    ndirs = [raw_input() for _ in xrange(N)]
    mdirs = [raw_input() for _ in xrange(M)]
    ans = solve(N,M,ndirs,mdirs)
    print "Case #%d: %s" % (t+1,ans)
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
