import sys

lines = sys.stdin.readlines()
num_cases = int(lines[0])
lines = lines[1:]

def calc_time_to_win(cps, g):
  return g/float(cps)

for i in range(1, num_cases+1):
  line = lines[0].strip().split(' ')
  lines = lines[1:]
  # cost of farm, cps/farm, goal
  c = float(line[0])
  f = float(line[1])
  x = float(line[2])
  farms = 0

  current_cookies = 0.0
  current_time = 0.0
  cps = 2.0

  # While we aren't finished
  while current_cookies < x:
    if current_cookies < c:
      if c < x:
        # Get the remaining cookes
        current_time +=    (c-current_cookies)/cps
        current_cookies += (c-current_cookies)
      else:
        current_time = x/cps
        current_cookies = x
      continue
    # If we would finish faster with one more farm,
    time_to_finish_with_one_farm = calc_time_to_win(cps+f, x-(current_cookies-c))
    time_to_finish_now = calc_time_to_win(cps, x-current_cookies)
    if time_to_finish_with_one_farm < time_to_finish_now:
      cps += f
      current_cookies = 0
      # Buy the farm
    # Else
    else:
      # Advance to end
      current_time += (x-current_cookies)/cps
      current_cookies = x
  print "Case #%s: %s" % (i, current_time)
