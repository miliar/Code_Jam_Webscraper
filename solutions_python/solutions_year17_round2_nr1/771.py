import itertools
import logging
import sys

def solve():
  return 1

def main():
  t = int(raw_input())
  for case in xrange(1, t + 1):
    d,n = [ int(j) for j in raw_input().split(" ") ]
    t_max = 0
    for i in range(n):
      di, si = [ float(j) for j in raw_input().split(" ") ]
      logging.debug("di=%i, si=%i" % (di, si) )
      t_max = max(t_max, (d-di)/si)
      r = float(d)/t_max
    print "Case #{}: {}".format(case, r)

if len(sys.argv) > 1 and sys.argv[1] == '-v':
  print "debug"
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

sys.setrecursionlimit(10100)
main()

