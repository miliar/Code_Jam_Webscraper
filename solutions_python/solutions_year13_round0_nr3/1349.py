import math

NNN = int(raw_input())
for nnn in xrange(1, NNN+1):
  print "Case #%d:" % (nnn),
  I = [int(x) for x in raw_input().split()]
  r = 0
  for i in xrange(int(math.ceil(math.sqrt(I[0]))), int(math.sqrt(I[1]))+1):
    a = str(i)
    b = len(a)
    if a[:b/2] == a[:(b-1)/2:-1]:
      a = str(i*i)
      b = len(a)
      if a[:b/2] == a[:(b-1)/2:-1]:
        r += 1
  print r
