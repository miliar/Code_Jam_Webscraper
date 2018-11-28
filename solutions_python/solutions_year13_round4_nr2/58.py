def solve():
  N,P = map(int,raw_input().split())
  N = 2**N
  low = 0
  high = N-1
  while low < high:
    mid = (low+high+1)/2
    worse = N-mid-1
    better = mid
    rank = worst_rank(worse,better,N)
    if rank < P:
      low = mid
    else:
      high = mid-1
  a = low
  low = 0
  high = N-1
  while low < high:
    mid = (low+high+1)/2
    worse = N-mid-1
    better = mid
    rank = best_rank(worse,better)
    if rank < P:
      low = mid
    else:
      high = mid-1
  b = low
  return str(a) + ' ' + str(b)
  
def best_rank(worse,better):
  if (worse == 0):
    return better
  if (better == 0):
    return 0
  better = (better+1)/2
  worse = (worse-1)/2
  return best_rank(worse, better)

def worst_rank(worse,better,N):
  b = best_rank(better,worse)
  return N-1-b

n_cases = input()
for case in range(1,n_cases+1):
  print 'Case #%d: %s' % (case, str(solve()))
