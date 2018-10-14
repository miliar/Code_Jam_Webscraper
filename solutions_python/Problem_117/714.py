def hor(grass, N, M, linenum, level):
  #value = grass[linenum][0]
  for i in xrange(M):
    if grass[linenum][i] > level:
      return False
  return True

def vert(grass, N, M, columnum, level):
  #value = grass[0][columnum]
  for i in xrange(N):
    if grass[i][columnum] > level:
      return False
  return True

def verify(grass, accounted, N, M, level):
  for j in xrange(N):
    for i in xrange(M):
      if grass[j][i] == level and not accounted[j][i]:
        return False
  return True

def lengths(grass):
  ret = set()
  for line in grass:
    for level in line:
      if level not in ret:
        ret.add(level)
  return ret

def unaccounted(accounted):
  for line in accounted:
    for letter in line:
      if not letter:
        return True
  return False

times = int(raw_input())
for time in xrange(times):
  N,M = map(int,raw_input().split(" "))
  grass = []
  for i in xrange(N):
    grass.append(map(int,raw_input().split()))

  levels = list(lengths(grass))
  levels.sort()
  
  answer = True

  for level in levels:
    accounted = [[False]*M]*N
    for j in xrange(N):
      for i in xrange(M):
        if vert(grass,N,M,i,level):
          for a in xrange(N):
            accounted[a][i] = True
      if hor(grass,N,M,j,level):
        accounted[j] = [True]*M
    if not verify(grass, accounted, N, M, level):
      answer = False
      break
        
  print "Case #%d: %s" % (time+1, "YES" if answer else "NO")
