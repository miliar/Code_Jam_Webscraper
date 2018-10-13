Dirs = {
  '^': (-1, 0),
  'v': (1, 0),
  '<': (0, -1),
  '>': (0, 1),
  }

for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  R, C = map(int, raw_input().split())
  M = []
  for _ in xrange(R):
    M.append(raw_input())
  def go(r, c, d):
    r += Dirs[d][0]
    c += Dirs[d][1]
    while 0 <= r < R and 0 <= c < C:
      if M[r][c] != '.':
        return True
      r += Dirs[d][0]
      c += Dirs[d][1]
    return False
  def count():
    cnt = 0
    for r in xrange(R):
      for c in xrange(C):
        if M[r][c] != '.':
          if go(r, c, M[r][c]):
            continue
          ok = False
          for d in '^v<>':
            if d == M[r][c]:
              continue
            if go(r, c, d):
              ok = True
              break
          if ok:
            cnt += 1
          else:
            return -1
    return cnt
  ans = count()
  if ans == -1:
    print "IMPOSSIBLE"
  else:
    print ans
