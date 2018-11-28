
def dict_inc(x, k, v):
  if k > 0:
    if k in x:
      x[k] += v
    else:
        x[k] = v

def step(gaps):
  gaps = dict(gaps.items())
  gap = max(gaps)
  gap_cnt = gaps[gap]
  del gaps[gap]
  dict_inc(gaps, gap // 2, gap_cnt)
  dict_inc(gaps, (gap - 1) // 2, gap_cnt)
  return gaps

def destructure_gap(gaps, gap, gap_cnt):
  gaps = dict(gaps.items())
  del gaps[gap]
  dict_inc(gaps, gap // 2, gap_cnt)
  dict_inc(gaps, (gap - 1) // 2, gap_cnt)
  return gaps
  
def test(N, K):
  gaps = {N:1}
  while True:
    gap = max(gaps)
    gap_cnt = gaps[gap]
    if K <= gap_cnt:
      return (gap // 2, (gap - 1) // 2)
    gaps = destructure_gap(gaps, gap, gap_cnt)
    K -= gap_cnt

T = int(input())
for i in range(T):
  N, K = map(int, input().split())
  print("Case #{}: {} {}".format(i + 1, *test(N, K)))