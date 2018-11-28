import sys
import time
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def dig(c): return ord(c) - 48

t00 = time.clock()

        
def solve(candies):
    b = reduce(lambda x,y: x ^ y, candies)
    if b:
        return -1
    
    candies.sort()
    s = reduce(lambda x,y: x + y, candies)
    c1 = candies[0]
    return s - c1

for t in range(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    N = readint()
    candies = readarray(int)
    ans = solve(candies)
    print "Case #%d:" % (t+1),
    if ans < 0:
        print "NO"
    else:
        print ans
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
