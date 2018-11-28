#!/usr/bin/python -tt

def main(C, F, X):
  Fr = 2.0
  T0 = 0.0
  Tr = T0 + X / Fr
  Tm = T0 + C / Fr + X / (Fr + F)
  while Tm < Tr:
    T0 += C / Fr
    Fr += F
    Tr = T0 + X / Fr
    Tm = T0 + C / Fr + X / (Fr + F)
  return Tr


if __name__ == '__main__':
  import sys
  T = int(sys.stdin.readline())
  for i in xrange(T):
    C, F, X = map(float,sys.stdin.readline().strip().split(" ")) 

    res = main(C, F, X)
    print "Case #%d: %.7f" % (i + 1, res)

