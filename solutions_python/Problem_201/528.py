import sys

def solve(n,k):
  if k == 1:
    if n == 1:
      return [0,0]
    else:
      (l,x) = divmod(n-1, 2)
      if x == 0:
        m = l
      else:
        m = l + 1
      return [m,l];
  else:
    (n1,m1) = divmod(n-1, 2)
    (k1,m2) = divmod(k-1, 2)
    
    if m1 == 0:
        n2 = n1
    else:
        n2 = n1 + 1
    if m2 == 0:
      k2 = k1
    else:
      k2 = k1 + 1
    if(n1 == n2):
      print [n1,k2]
      return solve(n1,k2)
    else:
      if k1 == k2:
        print [n1,k1]
        return solve(n1,k1)
      else:
        print [n2,k2]
        return solve(n2,k2)

name = "C-large"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = long(f.readline().strip())

for t in xrange(T):
    line = f.readline().strip().split(' ')
    print line
    (n,k) = map(long, line)
    res = solve(n, k)
    
    s = "Case #%d: %d %d\n" % (t+1, res[0] , res[1])
    print s
    o.write(s)
