def get_time(cookies_per_second, farm_rate, farm_costs, target_cookies):
  time = 0
  while True:
    time_to_target_without_purchase = target_cookies / cookies_per_second
    time_until_purchase = farm_costs / cookies_per_second
    time_to_target_with_purchase = (target_cookies / (cookies_per_second + farm_rate)) + time_until_purchase

    if time_to_target_without_purchase < time_to_target_with_purchase:
      return time_to_target_without_purchase + time
    cookies_per_second = cookies_per_second + farm_rate
    time = time + time_until_purchase

cases = input()
for case in xrange(1, cases+1):
  line = raw_input().split()
  result = get_time(2.0, float(line[1]), float(line[0]), float(line[2]))
  print "Case #%d: %.7f" %(case, result)
