cases = int(raw_input())
for z in xrange(1, cases+1):
  x,r,c = map(int, raw_input().split())
  a = 'RICHARD'
  if x<7 and (r*c)%x == 0:
    w = max(r,c)
    h = min(r,c)
    if ((x==1 and r==1 and c==1) or
        (x==2 and w >= 2) or
        (x <= w and h >= int(x/2)+1) or
        (x==6 and x<=w and h>=3)):
      a = 'GABRIEL'
  print "Case #" + str(z) + ": " + str(a)
