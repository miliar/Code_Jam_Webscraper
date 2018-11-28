import sys

def solve(C,F,X):
    C,F,X = float(C),float(F),float(X)
    t = 0.0
    p = 2.0
    while True:
       pos1 = X/p
       pos2 = C/p + X/(p+F)
       if pos1 <= pos2:
          t += pos1
          return t
       t += C/p
       p += F

    return 0  # nunca llega aqui

# main()

# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    C,F,X = [float(w) for w in sys.stdin.readline().split()]

    best = solve(C,F,X)
    print 'Case #%d: %.7f' % (tc, best)


