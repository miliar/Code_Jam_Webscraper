dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dm = {">": 0, "v": 1, "<": 2, "^": 3}

T = int(raw_input())
for t in range(1, T+1):
  R,C = map(int, raw_input().split())
  g = []
  for r in range(R):
    g.append(raw_input())
  res = 0
  pos = True
  for r in range(R):
    for c in range(C):
      if g[r][c] in dm:
        good = [False]*4
        for d in range(4):
          nr = r
          nc = c
          while True:
            nr += dr[d]
            nc += dc[d]
            if nr >= 0 and nr < R and nc >= 0 and nc < C:
              if g[nr][nc] != ".":
                good[d] = True
            else:
              break
        d = dm[g[r][c]]
        if good[d]:
          continue
        if not sum(good):
          pos = False
        else:
          res += 1
  print "Case #%d: %s" % (t, "IMPOSSIBLE" if not pos else str(res))
