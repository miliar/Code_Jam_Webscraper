I = (0,1,0,0)
J = (0,0,1,0)
K = (0,0,0,1)

quat = { 'i': I, 'j': J, 'k': K }

def qprod(s,t):
  a1,b1,c1,d1 = s
  a2,b2,c2,d2 = t
  r = []
  r.append(a1*a2 - b1*b2 - c1*c2 - d1*d2)
  r.append(a1*b2 + b1*a2 + c1*d2 - c2*d1)
  r.append(a1*c2 - b1*d2 + c1*a2 + d1*b2)
  r.append(a1*d2 + b1*c2 - c1*b2 + d1*a2)
  return tuple(r)


def allTriples():
  import itertools as it
  return it.product((I,J,K),repeat=3)

#for t in allTriples():
#  print t, ": ", qprod(t[0],qprod(t[1],t[2]))

def solve(H,X,L):

  LL = map(lambda x: quat[x], list(H)) 
  V = reduce(lambda x,y: qprod(x,y), LL * ( X % 4 ), (1,0,0,0))

  if V != (-1,0,0,0):
    return "NO"

  E = min(4,X)
  Q = LL * E
 
  # Index of leftmost prefix evaluating to I
  i = -1
  current = (1,0,0,0)
  for q in Q:
    i += 1
    current = qprod(current,q)
    if current == I:
      break

  if current != I:
    return "NO"

  # Index of rightmost prefix evaluating to K
  k = L*E
  assert len(Q) == k
  current = (1,0,0,0)
  for q in reversed(Q):
    k -= 1
    current = qprod(q,current)
    if current == K:
      break

  if current != K:
    return "NO"

  if i < k or ( X > 4 and i - k + 1 + E * L <= L * X ):
    return "YES"

  return "NO"

if __name__ == '__main__':

  T = int(raw_input())
  for t in xrange(T):
    L,X = map(int,raw_input().strip().split(' '))
    H = raw_input().strip()
    print "Case #%d: %s" % (t+1, solve(H,X,L))


