def doCase(ln):
  numbers = [int(c) for c in ln.split()]
  xor_s = reduce(lambda x, y: x ^ y, numbers)
  if xor_s:
    return 'NO'
  sum_s = sum(numbers)
  return sum_s - min(numbers)
  
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  n = int(stdin.readline())
  ln = stdin.readline()
  
  val = doCase(ln)
  print 'Case #%s: %s' % (i+1, val )