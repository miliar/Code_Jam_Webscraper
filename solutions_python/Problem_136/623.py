ntc = input()
for itc in range(ntc):
  c, f, x = map(float, raw_input().split())

  lb = 0
  ub = 10**6
  vals = []
  vals.append(0.0)
  time = 0.0
  profit = 2.0
  for _ in range(ub+1):
    time += c / profit
    vals.append(time)
    profit += f
  best = x / 2.0
  rate = 2.0
  def TV(i):
    return vals[i] + x / (2.0 + i * f)
  while lb <= ub:
    if ub - lb <= 5:
      for i in range(lb, ub+1):
        best = min([best, TV(i)])
      break
    else:
      rng = (ub - lb) / 3
      low = lb + rng
      hi = lb + rng * 2
      vallow = TV(low)
      valhi = TV(hi)
      best = min([best, vallow, valhi])
      if vallow < valhi:
        ub = hi-1
      else:
        lb = low+1

  res = best
  print 'Case #{0}: {1}'.format(itc+1, '%.8f' % res)


