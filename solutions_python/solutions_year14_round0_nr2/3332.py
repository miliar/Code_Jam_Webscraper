T = int(raw_input().strip())

for case_n in range(1, T+1):
  C, F, X = map(float, raw_input().strip().split())
  memo = {i : C / (2.0 + (i - 1) * F) for i in range(1, int(X * 10))}
  min_cost = X / 2.0
  n, t = 1, min_cost
  while t <= min_cost:
    t = (X / (2.0 + n * F)) + sum(memo[i] for i in range(1, n+1))
    if t < min_cost:
      min_cost = t
    n += 1
  print("Case #%d: %.07f" %(case_n, min_cost))
