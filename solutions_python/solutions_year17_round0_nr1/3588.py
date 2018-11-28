t = int(raw_input())

for a in range(t):
  x = 0
  q = raw_input()
  (q,r) = q.split(" ")
  r = int(r)
  for b in q:
    x <<= 1
    if b == "+":
      x += 1
  ans = pow(2, len(q))-1
  #print ans
  if x == ans:
    print "Case #%d: 0" % (a+1)
    continue
  z = 0
  flip = pow(2,r)-1
  for c in range( len(q) - r + 1):
    if ((x >> c) & 1) == 0:
      x = x ^ (flip << c)
      z += 1
      #print x
  if x != ans:
    print "Case #%d: IMPOSSIBLE" % (a+1)
  else:
    print "Case #%d: %d" % (a+1,z)

