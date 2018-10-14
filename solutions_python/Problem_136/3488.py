MAX_FARMS = 8000

cases = input()

for case in xrange(1, cases+1):
  cfx_input = raw_input()
  cfx_input = cfx_input.split(' ')
  C = float(cfx_input[0])
  F = float(cfx_input[1])
  X = float(cfx_input[2])

  cost = [0]
  for num_farms in range(1, MAX_FARMS):
    cost.append(cost[num_farms-1] + (C / (2.0 + F * (num_farms-1))) )

  time = [X / 2.0]
  for num_farms in range(1, MAX_FARMS):
    time.append(X / (2.0 + num_farms * F))

  final_cost = []
  for (c, t) in zip(cost, time):
    final_cost.append(c+t)

  print 'Case #%d: %.7f' % (case, min(final_cost))





