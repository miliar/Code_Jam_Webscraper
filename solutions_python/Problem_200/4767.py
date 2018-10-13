from itertools import *

t = int(raw_input())
for i in xrange(1, t + 1):
  n = int(raw_input())
  for j in islice(count(n, -1), None):
      if "".join(sorted(str(j))) == str(j):
          print "Case #{}: {}".format(i,j)
          break
