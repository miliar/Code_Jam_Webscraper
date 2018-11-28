from math import log
T = int(raw_input())

def bestplace(x,n):
  p = 2**n
  amt = int(log(p-x,2))
  print('x = %d, n = %d' %(x,n))
  print("amt = "+str(amt))
  tot = 0
  for i in xrange(n):
    tot *= 2
    if amt > 0:
      tot += 1
      amt -= 1
  print('p = %d tot = %d' % (p,tot))
  return p-tot

for kei in xrange(T):
  N,P = [int(x) for x in raw_input().split()]
  b1, b2 = -1,-1
  if P == 1:
    b2 = 0
  else:
    low = 0
    diff = 2**(N-1)
    cplace = 1
    while True:
      low += diff
      diff /= 2
      cplace *= 2
      if cplace > P:
        break
      b2 = low
  if P == 2**N:
    b1 = 2**N-1
  else:
    high = 0
    diff = 2
    cplace = 1
    cdiff = 2**(N-1)
    while cplace <= P:
      b1 = high
      high += diff
      diff *= 2
      cplace += cdiff
      cdiff /= 2
  print('Case #%d: %d %d' % (kei+1, b1, b2))