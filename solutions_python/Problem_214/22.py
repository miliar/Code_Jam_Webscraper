import pycosat as ps

dirs = (
  (-1, 0), # UP
  (0, -1), # LEFT
  (1, 0),  # DOWN
  (0, 1)   # RIGHT
)

def dir_to_s(d):
  if d in (0, 2): return -1
  else: return 1

def reflect(d, c):
  if c == '/':
    return (3, 2, 1, 0)[d]
  elif c == '\\':
    return (1, 0, 3, 2)[d]

def go(G, i, j, d):
  res = set()
  si, sj = i, j
  while True:
    i, j = i + dirs[d][0], j + dirs[d][1]
    if i < 0 or i >= len(G) or j < 0 or j >= len(G[0]): return res
    if G[i][j] == '#': return res
    if G[i][j] in ('-', '|'):
      res.add((i, j, dir_to_s(d)))
    if G[i][j] in ('/', '\\'):
      d = reflect(d, G[i][j])
    if i == si and j == sj: return res

_T = int(raw_input())
for _t in range(1, _T+1):
  R, C = map(int, raw_input().split())
  G = [list(raw_input()) for _ in range(R)]
  
  D = dict()
  
  ok = True
  haveto = []
  for i in range(R):
    for j in range(C):
      if G[i][j] not in ('-', '|', '.'): continue
      
      vert = set()
      for d in (0, 2):
        vert.update(go(G, i, j, d))
      hori = set()
      for d in (1, 3):
        hori.update(go(G, i, j, d))
      if G[i][j] == '.':
        if len(vert) > 1: vert = set()
        if len(hori) > 1: hori = set()
        res = vert.union(hori)
        if len(res) == 0:
          ok = False
          break
        elif len(res) == 1:
          (si, sj, sd) = res.pop()
          if (si, sj) in D and D[si, sj] != sd:
            ok = False
            break
          elif (si, sj) not in D:
            D[si, sj] = sd
        else:
          (si1, sj1, sd1) = res.pop()
          (si2, sj2, sd2) = res.pop()
          haveto.append(((si1, sj1), sd1, (si2, sj2), sd2))
      else:
        if len(vert) > 0 and len(hori) > 0:
          ok = False
          break
        if len(vert) == 0 and len(hori) == 0: continue
        if len(vert) > 0: sd = 1
        if len(hori) > 0: sd = -1
        if (i, j) in D and D[i, j] != sd:
          ok = False
          break
        D[i, j] = sd
    if not ok:
      break
  if not ok:
    print 'Case #{}: IMPOSSIBLE'.format(_t)
    continue
  tmp = []
  for (p1, d1, p2, d2) in haveto:
    if p1 in D and D[p1] == d1: continue
    if p2 in D and D[p2] == d2: continue
    if p1 in D and p2 in D:
      ok = False
      break
    if p1 in D: D[p2] = d2
    elif p2 in D: D[p1] = d1
    else: tmp.append((p1, d1, p2, d2))
  if not ok:
    print 'Case #{}: IMPOSSIBLE'.format(_t)
    continue

  formula = []
  positions = []
  i = 1
  PTI = dict()
  for p in D:
    formula.append([i*D[p]])
    PTI[p] = i
    positions.append(p)
    i += 1
  for (p1, d1, p2, d2) in haveto:
    if p1 not in PTI:
      PTI[p1] = i
      positions.append(p1)
      i += 1
    if p2 not in PTI:
      PTI[p2] = i
      positions.append(p2)
      i += 1
    formula.append([PTI[p1]*d1, PTI[p2]*d2])

  res = ps.solve(formula)

  if not isinstance(res, list):
    print 'Case #{}: IMPOSSIBLE'.format(_t)
    continue

  for n in res:
    i, j = positions[abs(n)-1]
    if n < 0:
      G[i][j] = '|'
    else:
      G[i][j] = '-'

  print 'Case #{}: POSSIBLE'.format(_t)
  for i in range(R):
    print ''.join(G[i])
