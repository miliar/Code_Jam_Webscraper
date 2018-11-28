import sys

def cookie(C, F, X):
  step = 2.0
  best = X / step
  farms = 1
  while True:
    amount = 0
    step = 2.0 
    for farm in xrange(1, farms + 1):
      amount += (C / step)
      step += F
    amount += X / step
    if best < amount:
      break
    best = amount
    farms += 1
  return best

cases = int(sys.stdin.readline())
for case in xrange(1, cases + 1):
  line = sys.stdin.readline()
  p = [float(i) for i in line.split()]
  print "Case #%d: %.7f" % (case, cookie(p[0], p[1], p[2]))
