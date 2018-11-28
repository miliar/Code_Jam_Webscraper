from os import sys

def expected_time_of_win(cps, goal, time):
  return time + goal / cps

num_cases = int(sys.stdin.readline())

for case in range(1,num_cases+1):
  params = [float(s) for s in sys.stdin.readline().split()]
  cost = params[0]
  farm_production = params[1]
  goal = params[2]
  cps = 2
  time = 0

  best_etw = expected_time_of_win(cps, goal, time)
  while True:
    new_time = time + cost / cps
    new_cps = cps + farm_production
    new_etw = expected_time_of_win(new_cps, goal, new_time)
    if new_etw < best_etw:
      best_etw = new_etw
      time = new_time
      cps = new_cps
    else:
      break

  print "Case #" + str(case) + ":", best_etw
