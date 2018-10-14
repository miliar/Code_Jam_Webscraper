
for tot in xrange(input()):
  cost, single_rate, goal = map(float, raw_input().split())
  time_passed = 0.0
  current_rate = 2.0
  ans = 0
  while ans == 0:
    min_time = goal / current_rate
    time_for_next_farm = cost / current_rate
    if time_for_next_farm + goal / (current_rate + single_rate) < min_time:
      time_passed += time_for_next_farm
      current_rate += single_rate
    else:
      ans = time_passed + min_time
  print "Case #%d: %.7f" % (tot + 1, ans)

