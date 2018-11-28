import os.path
import sys

def shoot(y,x,G,P,R,C,L):
  canRotate = set([0,1])
  # horizontal
  # right
  k = 1
  while x+k<C and G[y][x+k]=='.':
    k += 1
  if x+k<C and G[y][x+k]!='#':
    canRotate.discard(0)
  else:
    #left
    k = 1
    while x-k<C and G[y][x-k]=='.':
      k += 1
    if x-k>=0 and G[y][x-k]!='#':
      canRotate.discard(0)
    if 0 in canRotate:
      k = 1
      while x+k<C and G[y][x+k]=='.':
        P[y][x+k] += [[L,0]]
        k += 1
      k = 1
      while x-k>=0 and G[y][x-k]=='.':
        P[y][x-k] += [[L,0]]
        k += 1
  
  # vertical
  # down
  k = 1
  while y+k<R and G[y+k][x]=='.':
    k += 1
  if y+k<R and G[y+k][x]!='#':
    canRotate.discard(1)
  else:
    # up
    k = 1
    while y-k>=0 and G[y-k][x]=='.':
      k += 1
    if y-k>=0 and G[y-k][x]!='#':
      canRotate.discard(1)
    if 1 in canRotate:
      k = 1
      while y+k<R and G[y+k][x]=='.':
        P[y+k][x] += [[L,1]]
        k += 1
      k = 1
      while y-k>=0 and G[y-k][x]=='.':
        P[y-k][x] += [[L,1]]
        k += 1

  return canRotate      


FS = []
def trySet(F,Q, L = 0, S = []):
  if F:
    X = F[0]
    for x in X:
      bad = False
      NQ = []
      for q in Q:
        nq = []
        good = False
        for qq in q:
          if qq[0] == L:
            good |= (qq[1] == x)
          else:
            nq += [qq]
        if not good and not nq:
          print L, qq
          # not possible to this way                    
          bad = True
          break     
        if nq and not good:               
          NQ += [nq]
      if not bad:
        if trySet(F[1:], NQ, L+1, S + [x]):
          return True
    return False        
  global FS  
  FS = S          
  return True
  
  
def solve(f):
  R,C = map(int,f.readline().split(' '))
  G = []
  P = []
  for _ in range(R):
    G += [f.readline().rstrip()]
    P += [[]]
    for _ in range(C):
      P[-1] += [[]]
  L = 0
  y = 0
  F = []
  for r in G:
    x = 0
    for c in r:
      if c in '-|':
        s = shoot(y,x,G,P,R,C,L)
        F += [list(s)]
        L += 1
        if not s:
          return "IMPOSSIBLE"
      x += 1
    y += 1

  Q = []
  y = 0
  for r in G:
    x = 0
    for c in r:
      if c in '.':
        if not P[y][x]:
          return "IMPOSSIBLE"
        Q += [P[y][x]]
      x += 1
    y += 1

  X = trySet(F,Q)
  if not X:
    return "IMPOSSIBLE"
  RES = "POSSIBLE"
  L = 0
  for r in G:
    RES += '\n'
    for c in r:
      if c in '-|':
        RES += '-|'[FS[L]]
        L += 1
      else:
        RES += c
  return RES  
  
def out(s):
  print s
  sys.stdout.flush()
  o.write(s)
  
if os.path.exists("input.in"):
  f = open("input.in")
else:
  f = open("input-sample.in")
o = open("output.out", "wt")
T = int(f.readline())
for t in range(T):
  out("Case #%d: %s" %(t+1,solve(f)))
  o.write('\n')
o.close()