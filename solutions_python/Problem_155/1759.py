cases = int(raw_input())
for z in xrange(1,cases+1):
  sm, s = map(str, raw_input().split())
  p = 0
  f = 0
  for y in xrange(int(sm)+1):
    #print y, f, p
    k = int(s[y])
    if p>=y :
      p += k
    elif k>0:
      f += y-p
      p = y+k
  print "Case #" + str(z) + ": " + str(f)
