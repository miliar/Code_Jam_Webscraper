
import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    s = sys.stdin.readline().split()[1]
    su = 0
    add = 0
    for index, value in enumerate(map(int, list(s))):
          if su < index:
              add += (index - su)
              su = index
          su += value
    print "Case #%d: %d" % (i+1, add)
