from collections import defaultdict

def LastPersonEmptySlots(N, K):
  """Returns the maximum and minimum of the gap for the K-th insertion on N + 2 stalls.

  Args:
    N: Number of stalls for users
    K: Number of people entering the bathroom

  Returns:
    max_gap: max(L_S, R_S)
    min_gap: min(L_S, R_S)
  """
  counter = defaultdict(int)
  counter[N] = 1
  n_person = 0
  while n_person < K:
    # Get the maximum element in the counter
    max_elem = max(counter.keys())
    curr_cnt = counter[max_elem]
    n_person += curr_cnt
    del counter[max_elem]
    # Insert sub-results in the counter
    max_gap = max_elem // 2
    min_gap = max_elem - max_gap - 1
    if max_gap: counter[max_gap] += curr_cnt
    if min_gap: counter[min_gap] += curr_cnt
  return (max_gap, min_gap)

T = int(input())
for i in range(1, T + 1):
  N, K = map(int, input().split(' '))
  max_gap, min_gap = LastPersonEmptySlots(N, K)
  print('Case #{}: {} {}'.format(i, max_gap, min_gap))
