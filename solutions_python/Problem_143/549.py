
nb_cases = int(raw_input())

for i in xrange(nb_cases):
  r = raw_input().split()
  a = int(r[0])
  b = int(r[1])
  k = int(r[2])
  cpt = 0
  for t in xrange(a):
    for l in xrange(b):
      if (t & l) < k:
        cpt += 1
  print("Case #%d: %d" % (i+1,cpt))
