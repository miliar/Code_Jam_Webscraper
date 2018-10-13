all_pairs = []
for n in xrange(1, 2000001):
  for i in xrange(1, 7):
    p = 10**i
    if p > n: break
    x, y = divmod(n, p)
    if 10*y < p or x == y: continue
    m = int(str(y) + str(x))
    if n < m and m <= 2000000:
      p1 = tuple(sorted([n, m]))
      all_pairs.append(p1)
all_pairs.sort()

T = int(raw_input())
for t in xrange(T):
  A, B = [int (i) for i in raw_input().split()]

  result = set()
  for n, m in all_pairs:
    if n > B: break
    if A <= n < m <= B:
      result.add((n, m))
  print "Case #%i:" % (t+1), len(result)
