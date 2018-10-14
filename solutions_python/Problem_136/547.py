import sys

test_cases = int(sys.stdin.readline().strip())

def time_to_win(cookie_rate, cookie_goal):
  return cookie_goal/cookie_rate

def time_to_buy_farm(farm_cost, cookie_rate):
  return farm_cost/cookie_rate

for test_case in range(test_cases):
  farm_cost, farm_rate, cookie_goal = [float(i) for i in sys.stdin.readline().strip().split(" ")]

  total_farms = 0
  total_time = 0
  cookie_rate = 2+(farm_rate*total_farms)

  if time_to_win(cookie_rate, cookie_goal) < time_to_buy_farm(farm_cost, cookie_rate):
    total_time = time_to_win(cookie_rate, cookie_goal)
  else:
    current_time_to_win = time_to_win(cookie_rate, cookie_goal)
    new_cookie_rate = 2+(farm_rate*(total_farms+1))
    new_time_to_win = time_to_buy_farm(farm_cost, cookie_rate) + time_to_win(new_cookie_rate, cookie_goal)

    while current_time_to_win > new_time_to_win:
      total_time += time_to_buy_farm(farm_cost, cookie_rate)
      current_time_to_win = new_time_to_win

      total_farms += 1
      cookie_rate = new_cookie_rate

      current_time_to_win = total_time + time_to_win(cookie_rate, cookie_goal)
      new_cookie_rate = 2+(farm_rate*(total_farms+1))
      new_time_to_win = total_time + time_to_buy_farm(farm_cost, cookie_rate) + time_to_win(new_cookie_rate, cookie_goal)

    total_time = total_time + time_to_win(cookie_rate, cookie_goal)

  print "Case #%d: %.7f" % (test_case+1, total_time)
