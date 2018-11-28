def cost(cookies, n_per_house, cost_house):
  k = 0
  next_house = cost_house / (2.0 + k * n_per_house)
  total = 0.0
  current_finish = cookies / (2.0 + k * n_per_house)
  next_finish = next_house +  cookies / (2.0 + (k + 1) * n_per_house)
  while next_finish < current_finish:
    total += next_house
    k += 1
    next_house = cost_house / (2.0 + k * n_per_house)
    current_finish = cookies / (2.0 + k * n_per_house)
    next_finish = next_house +  cookies / (2.0 + (k + 1) * n_per_house)
  return total + current_finish


  return sum([cost_house / (2.0 + k * n_per_house) for k in range(n_houses)]) + cookies / (2.0 + n_houses * n_per_house)

n_runs = int(raw_input())
for i in range(n_runs):
  C, F, X  = map(float, raw_input().split(' '))
  # print C, F, X
  print 'Case #%d: %.7f' % (i + 1, cost(X, F, C))
