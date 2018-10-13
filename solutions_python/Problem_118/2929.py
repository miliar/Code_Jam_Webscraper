import math

def RevNum(n, partial=0):
    if n == 0:
        return partial
    return RevNum(n / 10, partial * 10 + n % 10)

def PerfectSquare(num):
  if num == 1: return True
  x = num // 2
  y = set([x])
  while x * x != num:
    x = (x + (num // x)) // 2
    if x in y: return False
    y.add(x)
  return True

ps = 0

for tc in xrange(1, int(raw_input()) + 1):
    a,b = raw_input().split()
    
    for num in xrange(int(a), int(b) + 1):

        if RevNum(num) == num:

            if PerfectSquare(num) == True:

                if RevNum(int(math.sqrt(num))) == int(math.sqrt(num)):
                    ps = ps + 1
                    
    print 'Case #%d: %d' % (tc, ps)
    ps=0
