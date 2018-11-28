from math import *
def gcd(x, y):
  if y==0:
    return x
  return gcd(y, x%y)
tn = int(raw_input())
for cn in range(tn):
  print 'Case #%d:' % (cn + 1),
  r1,r2 =map(int, raw_input().split('/'))

  g = gcd(r1, r2)
  #print r1,r2,g
  r1 = r1/g
  r2 = r2/g
  lr2 = int(log(r2)/log(2))
  l = 0
  if (2 ** lr2  == r2):
    #print lr2, l
    while r1 < r2:
      r1 *= 2
      l += 1
    print l
  else:
    print 'impossible'    
