def read_int():
  return map(int, raw_input().strip().split())


def solve0(n, k):
  tmp = 2**n
  return (k+1) & (tmp*2-1) == tmp


def solve(n, k):
  tmp = 2**n - 1
  return k & tmp == tmp


def main():
  nc, = read_int()
  for i in xrange(nc):
    n, k = read_int()
    result = "ON" if solve(n, k) else "OFF"
    print 'Case #%d: %s' % (i+1, result)



if __name__ == "__main__":
  main()
