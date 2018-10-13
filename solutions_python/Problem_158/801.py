import sys

cases = int(sys.stdin.readline())
for case in range(1,cases+1):
  print "Case #%s: " %case,
  x, r, c =  [int(i) for i in sys.stdin.readline().split()]
  r, c = min(r, c), max(r, c)

  if (r * c) % x != 0:
    print 'RICHARD'
    continue
        
  if x == 1:
    print 'GABRIEL'

  if x == 2:
    print 'GABRIEL'
    
  if x == 3:
    if r == 1:
      print 'RICHARD'
    else:
      print 'GABRIEL'
    
  if x == 4:
    if r <= 2:
      print 'RICHARD'
    else:
      print 'GABRIEL'