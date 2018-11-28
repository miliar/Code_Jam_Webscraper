import sys
MOD = 10000
magic = '_welcome to code jam'

def main():
  N = int(raw_input())
  print >>sys.stderr, N
  for i in range(N):
    print 'Case #%d:' % (i+1),
    S = raw_input()
    opt = [0] * len(magic)
    opt[0] = 1
    for s in S:
      for idx, c in enumerate(magic):
        if s == c:
          opt[idx] = (opt[idx] + opt[idx-1]) % MOD
    print '%04d' % opt[len(magic)-1]


if __name__ == '__main__':
  main()
