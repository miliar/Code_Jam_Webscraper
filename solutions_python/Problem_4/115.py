

def minProd(u, v):
  u.sort()
  v.sort()
  v.reverse()
  res = 0

  for x in range(len(u)):
    res += u[x] * v[x]
  return res




T = int(raw_input())

for i in range(1, T+1):
  n = int(raw_input())
  
  v1 = map(int, raw_input().split())
  v2 = map(int, raw_input().split())
  
  print 'Case #%d: %d' % (i, minProd(v1,v2))
    
