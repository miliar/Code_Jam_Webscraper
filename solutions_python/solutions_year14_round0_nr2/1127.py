import sys

def solve(C, F, X, rate):
  best = X / rate
  buytime = 0
  while buytime < X:
    buytime += C / rate
    rate += F
    buy = buytime + X / rate
    if buy < best:
      best = buy
    else:
      return best


def main():
  T = int(sys.stdin.readline())
  for i in xrange(T):
    global C, F, X
    (C, F, X) = [float(x) for x in sys.stdin.readline().split()]
    
    best = solve(C, F, X, 2.0)
    
    print "Case #%d: %.7f" % (i+1, best)

main()