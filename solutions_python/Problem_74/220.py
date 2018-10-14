import re
import time

def READ_LINE_ARRAY(f, T): return map(T, f.readline().split())
def RLS(f): return f.readline().strip()

#f = sys.stdin
#SET_NAME = "c:\_temp\A"
#SET_NAME = "c:\_temp\A-small-attempt0"
#SET_NAME = "c:\_temp\A_test"
SET_NAME = "c:\_temp\A-large"

f = open(SET_NAME + ".in")
fo = open(SET_NAME + ".out", mode="w")
clock = time.clock()

T = int(f.readline())

for testCase in range(1, T+1):
    line = f.readline().split()
    N = int(line[0])
    idx = 1
    bPos = 1
    oPos = 1
    bTime = 0
    oTime = 0
    t = 0
    for n in xrange(N):
        color = line[idx]; idx+=1
        pos = int(line[idx]); idx+=1
        if color == 'B':
            dPos = abs(pos - bPos)
            dT = t - bTime; assert dT >= 0
            dur = dPos - dT
            if dur > 0:
                t += dur
            t += 1
            bPos = pos
            bTime = t
        elif color == 'O':
            dPos = abs(pos - oPos)
            dT = t - oTime; assert dT >= 0
            dur = dPos - dT
            if dur > 0:
                t += dur
            t += 1
            oPos = pos
            oTime = t
        else:
            assert False

    print "Case #%d: %d" % (testCase, t)
    fo.write("Case #%d: %d\n" % (testCase, t))
f.close()
fo.close()
print "Elapsed ms: %.3f" % (time.clock() - clock)

