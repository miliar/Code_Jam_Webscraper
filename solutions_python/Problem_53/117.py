import sys

def a(j, n, k):
  p = 2**n
  k = k % p
  if k == (p - 1):
    print 'Case #%d: ON' % j
  else:
    print 'Case #%d: OFF' % j

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    n = int(f.readline())
    for j in range(1, n + 1):
      n, k = (int(x) for x in f.readline().split())
      a(j, n, k)
