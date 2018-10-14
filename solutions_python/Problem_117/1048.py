NNN = int(raw_input())
for nnn in xrange(1, NNN+1):
  print "Case #%d:" % (nnn),
  N, M = [int(x) for x in raw_input().split()]
  B = [[int(x) for x in raw_input().split()] for n in xrange(N)]

  possible = True
  for x in xrange(N):
    for y in xrange(M):
      a = B[x][y]
      for yy in xrange(M):
        if B[x][yy] > a:
          possible = False
          break
      if not possible:
        for xx in xrange(N):
          if B[xx][y] > a:
            possible = True
            break
        possible = not possible
      if not possible: break
    if not possible: break

  print "YES" if possible else "NO"
