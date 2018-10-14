import sys
C = 0
F = 0
X = 0

result_map = {}

def memoize(f):
  def inner(n):
    if n not in result_map:
      result_map[n] = f(n)
    return result_map[n]
  return inner


@memoize
def time(n):
  if n == 0:
    return X/2
  return time(n-1) - X/((n-1)*F + 2) + C/((n-1)*F + 2) + X/(n*F + 2)


if __name__ == '__main__':
  f = sys.stdin
  N = int(f.readline().strip())
  for n in range(N):
    C, F, X = (float(x) for x in f.readline().strip().split())
    result_map = {}
    best = time(0)
    fn = 1
    t = time(1)
    while t < best:
      best = t
      fn += 1
      t = time(fn)

    print('Case #%i: %.7f' % (n+1, best))
