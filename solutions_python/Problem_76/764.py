import sys
from operator import xor

def main(args):
  T = int(raw_input())
  for i in range(1, T+1):
    N = int(raw_input())
    C = map(int, raw_input().split())

    x = reduce(xor, C)
    if x:
      print 'Case #%d: NO' % i
    else:
      print 'Case #%d: %d' % (i, sum(C) - min(C))

if __name__ == '__main__':
  main(sys.argv)
