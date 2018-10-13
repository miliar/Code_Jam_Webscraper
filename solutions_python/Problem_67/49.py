C = int(raw_input())

for case in xrange(1, C+1):
  R = int(raw_input())
  bacteria = {}
  toupdate = {}
  for i in xrange(R):
    X1, Y1, X2, Y2 = map(int, raw_input().split())
    for x in xrange(X1, X2+1):
      for y in xrange(Y1, Y2+1):
        bacteria[(x,y)] = 1
        toupdate[(x+1,y)] = 1
        toupdate[(x,y+1)] = 1
  ans = 0
  while bacteria:
    #print bacteria, toupdate
    newbacteria = {}
    newtoupdate = {}
    for x,y in bacteria:
      if (x-1,y) in bacteria or (x,y-1) in bacteria:
        newbacteria[(x,y)] = 1
        newtoupdate[(x+1,y)] = 1
        newtoupdate[(x,y+1)] = 1
    for x,y in toupdate:
      if (x-1,y) in bacteria and (x,y-1) in bacteria:
        newbacteria[(x,y)] = 1
        newtoupdate[(x+1,y)] = 1
        newtoupdate[(x,y+1)] = 1
    bacteria = newbacteria
    toupdate = newtoupdate
    ans += 1

  print "Case #%d: %d" % (case, ans)

