import sys
import numpy as np
from multiprocessing import Pool

def solve1(V,X,r,c):
  if c == X:
    return '{0}'.format(V/r)
  else:
    return 'IMPOSSIBLE'
  

def solve(inp):
  V,X,sources = inp
  err = 0.00000000001
  if len(sources) == 1:
    r, c =sources[0]
    return solve1(V,X,r,c)
  if len(sources) == 2:
    r1,c1 = sources[0]
    r2,c2 = sources[1]
    if c1 == c2:
      return solve1(V,X,r1+r2,c1)
    if c1 == X:
      return solve1(V,X,r1,c1)
    if c2 == X:
      return solve1(V,X,r2,c2)
    if max(c1,c2) < X or min(c1,c2) > X: return 'IMPOSSIBLE'

    a = np.array([[r1, r2], [r1*c1, r2*c2]])
    b = np.array([V, V*X])
    t = np.linalg.solve(a,b)
    if min(t) < -err: return 'IMPOSSIBLE'
    return '{0}'.format(max(t))


  return 'IMPOSSIBLE'


if __name__ == '__main__':
  T = int(input())

  inputs = []

  for iCase in range(T):
    nvx = input().split(' ')
    n = int(nvx[0])
    v = float(nvx[1])
    x = float(nvx[2])
    sources = []
    for i in range(n):
      r, c = [float(fff) for fff in input().split(' ')]
      sources.append((r, c))
    inputs.append((v,x,sources))

  p = Pool(4)

  res = p.map(solve, inputs, 1)
  for iCase, r in enumerate(res):
    print('Case #{0}: {1}'.format(iCase+1, r))
