from fractions import gcd

for t in xrange(1, int(raw_input())+1):
  a = map(long, raw_input().split()[1:])    
  x = reduce(gcd, [abs(x-y) for x in a for y in a], 0)
  print 'Case #%d: %d' % (t, (x-a[0]%x)%x)