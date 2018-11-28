import sys
import math

f = open(sys.argv[1], 'r')

T = int(f.readline())
for t in xrange(0, T):
    print "Case #%d:" % (t+1),
    r, t = map(int, f.readline().split())[:2]
   
    print int(0.25 * (math.sqrt(4*r*r - 4*r + 8*t + 1) - 2*r + 1))
