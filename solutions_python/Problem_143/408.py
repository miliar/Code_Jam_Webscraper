import sys
import math

f = open(sys.argv[1])
n = int(f.readline())

for t in xrange(1,n+1):
    A,B,K = map(int, f.readline().strip("\n").split())
    
    x = int(math.floor(math.log(K, 2)))
    total = 0# 2**x * 2**x

    for a in xrange(0, A):
        for b in xrange(0, B):
            if a&b < K:
                total += 1

                
    print "Case #%d: %d" % (t, total)










