import sys

def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

def gcdv(t):
  res=0
  for x in t:
    res = gcd(res,x)
  return res

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  v = map(int,raw_input().split())
  N = v[0]
  t = v[1:]
  
  t.sort()
  d = [t[j]-t[0] for j in range(1,N)]
  T = gcdv(d)
  k = t[0]/T
  if t[0]%T != 0:
    k += 1
  y = k*T-t[0]

  res = y
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
