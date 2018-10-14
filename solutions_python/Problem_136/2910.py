#!/usr/bin/python
num_test_cases = int(raw_input())

for case_number in xrange(1, num_test_cases+1):
  line = raw_input().split()
  c = float(line[0])
  f = float(line[1])
  x = float(line[2])

  buy_time = 0
  gen_rate = 2
  time_win_if_wait = buy_time + x / gen_rate
  while True:
    buy_time += c / gen_rate
    time_win_if_buy = buy_time + (x / (gen_rate + f))
    if time_win_if_wait < time_win_if_buy:
      break
    time_win_if_wait = time_win_if_buy
    gen_rate += f

  print "Case #%d: %.7f" % (case_number, time_win_if_wait)



