t = int(raw_input())

for i in xrange(1, t + 1):
  
  d,n = [int(v) for v in raw_input().split(" ")]
  m = 0.0

  for j in xrange(1, n+1):
      k,s = [int(x) for x in raw_input().split(" ")]
      t = (d-k)*1.0/s
      m = t if (t > m) else m

  print "Case #{}: {}".format(i, d*1.0/m)
