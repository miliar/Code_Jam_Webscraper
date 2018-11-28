from pprint import pprint
import sys

def rl():
  return sys.stdin.readline().strip()

def parse():
  N, M = map(int, rl().split())
  pat = []
  for _ in xrange(N):
    pat.append(map(int, rl().split()))
  return (N, M, pat)

def check(inp):
  N, M, pat = inp

  def is_edge(i, j):
    return (i == 0 and j == 0) \
      or (i == 0 and j == M-1) \
      or (i == N-1 and j == 0) \
      or (i == N-1 and j == M-1)

  min_val = 101
  for i in xrange(N):
    for j in xrange(M):
      if pat[i][j] < min_val:
        min_val = pat[i][j]

  same_row_min = []
  for i in xrange(N):
    final = True
    for j in xrange(M):
      if pat[i][j] != min_val:
        final = False
        break
    same_row_min.append(final)

  same_col_min = []
  for j in xrange(M):
    final = True
    for i in xrange(N):
      if pat[i][j] != min_val:
        final = False
        break
    same_col_min.append(final)

  for i in xrange(N):
    for j in xrange(M):
      if pat[i][j] == min_val and not same_row_min[i] and not same_col_min[j]:
        return False
  return True

def solve(inp):
  N, M, _ = inp
  if N == 1 or M == 1:
    return "YES"
  if not check(inp):
    return "NO"
  return "YES"

def main():
  cases = int(rl())
  for c in xrange(1, cases+1):
    inp = parse()
    res = solve(inp)
    print "Case #%d: %s" % (c, res)

main()
