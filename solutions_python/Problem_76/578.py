import operator

f = open('C-large.in', 'r')
cases = int(f.next())
for i in xrange(cases):
  f.next() # Skip number of candies
  candies = [int(x) for x in f.next().split()]
  
  if reduce(operator.xor, candies) != 0:
    print "Case #%d: NO" % (i + 1)
    continue
  
  candies.sort()
  print "Case #%d: %d" % (i + 1, sum(candies[1:]))