from collections import defaultdict
seen = [0]*1000


def findpairs(a, b):
  recycled_pairs = []
  for i in range(a, b):
    for k in range(1, len(str(i))):
      si = str(i)
      j = int(si[k:] + si[0:k])
      if len(str(j)) != len(str(i)): continue
      mn = min(j, i)
      mx = max(j, i)
      if a <= mn < mx <= b:
        recycled_pairs.append((mn, mx))
  return list(set(recycled_pairs))

n = int(raw_input())

for i in range(n):
  a, b = map(lambda x: int(x), raw_input().split())
  print "Case #%d: %d" % (i+1, len(findpairs(a,b)))
