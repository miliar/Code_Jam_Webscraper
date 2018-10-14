def solve(a, b, k):
  c = 0
  for A in xrange(a):
    for B in xrange(b):
      if A & B < k:
        c += 1
  return c

def main():
  T = int(raw_input())
  for t in xrange(1, T+1):
    a, b, k = map(int, raw_input().split())
    print "Case #{0}: {1}".format(t, solve(a, b, k))

if __name__ == '__main__':
  main()
