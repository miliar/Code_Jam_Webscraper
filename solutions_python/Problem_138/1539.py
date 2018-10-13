#!/usr/bin/env python
import sys

def main(argv=None):
  if argv is None:
    argv = sys.argv

  T = int(sys.stdin.readline())
  for t in xrange(T):
    sys.stdin.readline()
    naomi = map(float, sys.stdin.readline().split(" "))
    ken = map(float, sys.stdin.readline().split(" "))
    
    # War
    wn = 0
    wk = 0
    warnaomi = list(naomi)
    warken = list(ken)
    warnaomi.sort()
    warken.sort()
    for b in naomi:
      c = 0
      remaining = len(warken)
      while remaining == len(warken) and c < remaining:
        # Smallest block to score a point
        if warken[c] > b:
          del warken[c]
          wk += 1
        c += 1
      
      # Cannot score a point - get rid of smallest block
      if remaining == len(warken):
        del warken[0]
        wn += 1
    
    # Deceitful war
    dn = 0
    dk = 0
    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    for b in naomi:
      c = 0
      remaining = len(ken)
      while remaining == len(ken) and c < remaining:
        # How many Naomi-Ken pairs of blocks are there so that Naomi's has
        # greater mass than Ken's?
        if b > ken[c]:
          del ken[c]
          dn += 1
        c += 1
      
      # Cannot score a point - get rid of smallest block
      if remaining == len(ken):
        del ken[-1]
        dk += 1
    
    print "Case #%d: %d %d" % (t + 1, dn, wn)

if __name__ == "__main__":
	sys.exit(main())

