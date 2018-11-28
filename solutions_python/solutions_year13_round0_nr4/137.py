#!/usr/bin/env python

T = int(raw_input())

dead_paths = set()

def dfs(chests, unused_keys, closed_chests, path):
  #print 'p', closed_chests, unused_keys, path
  if len(closed_chests) == 0:
    return path
  if tuple(closed_chests) in dead_paths:
    return None
  for chest in closed_chests:
    try:
      key_idx = unused_keys.index(chests[chest][0])
      keys = unused_keys[:] + chests[chest][1]
      del keys[key_idx]
      closed = closed_chests[:]
      closed.remove(chest)
      v = dfs(chests, keys, closed, path + [chest])
      if v:
        return v
    except ValueError:
      pass
  dead_paths.add(tuple(closed_chests))
  return None

def read_problem():
  K, N = [ int(e) for e in raw_input().split() ]
  k = [ int(e) for e in raw_input().split() ]
  c = []
  for i in range(N):
    v = [ int(e) for e in raw_input().split() ]
    c.append((v[0], v[2:]))
  return k, c

def solve(problem):
  global dead_paths
  k, c = problem
  #print k
  #for cc in range(len(c)):
  #  print cc, c[cc]
  dead_paths = set()
  res = dfs(c, k, range(len(c)), [])
  if res:
    return " ".join([str(r+1) for r in res])
  else:
    return "IMPOSSIBLE"

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

