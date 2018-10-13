import itertools

def read_ints():
  return map(int, raw_input().split())

def solve(A, B, K):
  ans = 0
  for a in range(A):
    for b in range(B):
      if a & b < K:
	ans += 1
  return ans

for test in range(1, int(raw_input()) + 1):
  A, B, K, = read_ints()
  sol = solve(A, B, K)
  print "Case #%d: %d" % (test, sol)