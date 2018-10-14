def read_int(): return int(raw_input())
def read_arr(): return map(lambda s: {'+': 1, '-': -1}[s], raw_input().split())  


def solve(arr):
  cakes = map(lambda s: {'+': 1, '-': -1}[s], arr[0])
  k = int(arr[1])
  n = len(cakes)

  i = 0
  flip = 0
  while i + k - 1 < n:
    if cakes[i] < 0:
      cakes[i:i+k] = [-1 * _ for _ in cakes[i:i+k]]
      flip += 1
    i += 1

  if not all(x > 0 for x in cakes):
    return 'IMPOSSIBLE'

  return flip

T = read_int()

for t in xrange(T):
  print 'Case #%d: %s' % (t+1, solve(raw_input().split()))