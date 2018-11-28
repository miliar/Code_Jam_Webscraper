import sys
import time
import math

def RLA(f, T): return map(T, f.readline().split())

def Check(x):
    digs = []
    while x >= 10:
        digs += [x%10]
        x = x // 10
    digs += [x]
    L = len(digs) #4 for "1221"
    #print digs
    for i in range(L//2):
        if digs[i] != digs[L-i-1]:
            return False
    return True

def Solve(A, B):
    cnt = 0
    a = int(math.sqrt(A))-1
    b = int(math.sqrt(B))+2
    for x in range(a,b+1):
        sq = x*x
        if sq < A or sq > B:
            continue
        if Check(x) and Check(sq):
            cnt+=1
    return cnt

f = open(r"C:\_temp\C-small-attempt0.in"); TT, = RLA(f, int)
fo = open(r"C:\_temp\C-small-attempt0.out", mode="w")

#f = sys.stdin; TT=1
#fo = sys.stdout
dbg = sys.stderr

assert Check(0)
assert Check(1)
assert Check(9)
assert Check(11)
assert Check(121)
assert Check(1221)
assert not Check(12)
assert not Check(122)
assert not Check(1231)
assert Check(12345678987654321)

clock = time.clock()
for tt in xrange(TT):
    A, B = RLA(f, int)
    ans = Solve(A,B)
    fo.write("Case #%d: %d\n" % (tt+1, ans))
    dbg.write("Case %d\n" % tt)
f.close()
fo.close()
dbg.write("Elapsed s: %.3f\n" % (time.clock() - clock))
