from collections import defaultdict

T = input()
for tc in range(1, T+1):
  N, X = [int(x) for x in raw_input().split()]
  S = [int(x) for x in raw_input().split()]
  m = defaultdict(int)
  for s in S:
    m[s] += 1
  ct = 0
  for i in range(X, X/2, -1):
    if m[i] > 0:
      ct += m[i]
      left = m[i]
      for j in range(X - i, 0, -1):
        if left > 0 and m[j] > 0:
          rem = min(left, m[j])
          m[j] -= rem
          left -= rem
  ct2 = 0
  for i in range(X/2, 0, -1):
    if m[i] > 0:
      ct2 += m[i]
  print "Case #" + str(tc) + ":", ct + (ct2 + 1) / 2