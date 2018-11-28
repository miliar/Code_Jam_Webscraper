def allLessThan(P, x):
  for y in P:
    if y >= x:
      return False
  return True

def solve(D, P):
  if allLessThan(P, 1):
    # empty already
    return 0
  elif allLessThan(P, 2):
    return 1
  else:
    # eat case
    # each people eat one if possible
    P2 = P[:]
    for i in range(len(P2)):
      if P2[i] > 0:
        P2[i] = P2[i] - 1
    res = solve(D, P2) + 1

    # move case
    Ps = sorted(P)
    Ps.reverse()
    maxP = Ps[0]
    for i in range(2, maxP/2+1):
      # move i to empty plate 
      Pi = Ps[:]
      Pi[0] -= i
      Pi.append(i)
      res = min(res, solve(D, Pi) + 1)
    return res
      

f = open('B-small-attempt5.in', 'r')
#f = open('test.in', 'r')
T = int(f.readline())
for i in range(T):
  D = int(f.readline())
  P = map(int, f.readline().split())
  print 'Case #%d: %d' % (i+1, solve(D, P))
