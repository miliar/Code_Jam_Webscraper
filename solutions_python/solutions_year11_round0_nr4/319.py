def oop(ls):
  return sum(a != b for a, b in zip(ls, xrange(1, len(ls) + 1)))

f = open('D-large.in', 'r')
cases = int(f.next())
for i in xrange(cases):
  f.next()
  numbers = [int(x) for x in f.next().split()]
  print "Case #%d: %.6f" % (i + 1, oop(numbers))