import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ R, C ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  lines = []
  for r in xrange(R):
    line = sys.stdin.readline().strip()
    lines.append(line)
  res = 0
  can_do = True
  for r in xrange(R):
    for c in xrange(C):
      dr, dc = 0, 0
      if lines[r][c] == '<': dc = -1
      elif lines[r][c] == '>': dc = 1
      elif lines[r][c] == '^': dr = -1
      elif lines[r][c] == 'v': dr = 1
      else: continue
      ok = False
      rr, cc = r, c
      while True:
        rr += dr
        cc += dc
        if rr < 0 or R <= rr or cc < 0 or C <= cc: break
        if lines[rr][cc] != '.':
          ok = True
          break
      if ok: continue

      prev_dc, prev_dr = dc, dr
      res += 1
      ok = False
      for (dc, dr) in [ (-1, 0), (1, 0), (0, 1), (0, -1) ]:
        if dc == prev_dc and dr == prev_dr: continue
        rr, cc = r, c
        while True:
          rr += dr
          cc += dc
          if rr < 0 or R <= rr or cc < 0 or C <= cc: break
          if lines[rr][cc] != '.':
            ok = True
            break
        if ok: break
      if not ok: can_do = False
      if not can_do: break
    if not can_do: break

  res = "IMPOSSIBLE" if not can_do else str(res)
  print "Case #%d: %s" % (1+tmp_tc, res)

