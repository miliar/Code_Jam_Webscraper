from math import pow

t = int(raw_input())
for i in range(t):
  [n, k] = map(int, raw_input().split(' '))
  if k >= pow(2,n)-1 and (k+1)%pow(2,n) == 0:
    o = 'ON'
  else:
    o = 'OFF'
  print 'Case #%d: %s' % (i+1, o)
    
