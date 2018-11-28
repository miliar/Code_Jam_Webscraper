from sys import stdin

case_cnt = int(stdin.readline())

for case_no in range(1, case_cnt + 1):
  R, k, N = (int(x) for x in stdin.readline().split())
  g       = [int(x) for x in stdin.readline().split()]
  total_g = sum(g)

  if total_g <= k:
    result = R * total_g
  else:
    result = 0
    for round_no in range(R):
      people_cnt = 0
      while people_cnt + g[0] <= k:
        people_cnt += g[0]
        g.append(g.pop(0))
      result += people_cnt

  print('Case #{}: {}'.format(case_no, result))
