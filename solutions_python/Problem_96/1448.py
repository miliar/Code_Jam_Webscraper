from collections import defaultdict
import sys

table = {}
supr = {}
for i in range(0, 31):
  supr[i] = 11
  table[i] = 11
for s in range(0, 31):
  for a in range(0, 11):
    for b in range(0, 11):
      for c in range(0, 11):
        if a+b+c == s and max(a,b,c) - min(a,b,c) <= 2:
          if max(a,b,c) - min(a,b,c) == 2: # suprising
#            if s == 23:
#              print s,a,b,c, supr[s]
            supr[s] = min(supr[s], max(a,b,c))
          table[s] = min(table[s], max(a,b,c))

#for i in range(0, 31):
#  print i, table[i], supr[i]

def getnum():
  return [int(x) for x in sys.stdin.readline().split()]

T, = getnum()
for t in range(T):
  vals = getnum()
  N = vals[0]
  s = vals[1]
  p = vals[2]
  scores = vals[3:]
  scores.sort(reverse=True)
#  print N, s, p
  scores2 = [(i, table[i],supr[i]) for i in scores]
#  print scores2
  count = 0
  i = 0
  sup = 0
  idx = []
  while sup < s:
    if scores2[i][0] <= 28 and scores2[i][0] >= 2:
      if scores2[i][2] >= p:
        count += 1
      idx.append(i)
      sup += 1
    i += 1

  count = 0
  for i, c1, c2 in scores2:
    if s > 0:
      if c1 >= p:
        count += 1
      elif c1 < p and c2 >= p and c2 != 11:
        s -= 1
        count += 1
    else:
      if c1 >= p:
        count += 1
  print "Case #%d: %d" % (t+1, count)
  # Find best candidates for supr.
  
#  break

