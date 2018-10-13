import math

input_n = int(raw_input())
nn = []
mm = []
dd = []

for i in xrange(input_n):
  n,m = tuple( [ int(x) for x in raw_input().strip().split()])
  nn.append(n)
  mm.append(m)

min_n = min(nn)
max_m = max(mm)

sq_n = int(math.ceil(math.sqrt(min_n)))
sq_m = int(math.sqrt(max_m))

for i in xrange(sq_n,sq_m+1):
  si = str(i)
  if si == si[::-1]:
    k = str(i**2)
    if k == k[::-1]:
      dd.append(i**2)

for i in xrange(input_n):
  r = 0
  for e in dd:
    if e>=nn[i] and e<=mm[i]:
      r+=1
    elif e>mm[i]:
      break;

  print "Case #%d: %s" % ((i+1),r)

