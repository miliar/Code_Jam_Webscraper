def read_floats():
  return map(float, raw_input().split())

def solve(cost, speed_bonus, goal):
  elapsed = 0.0
  speed = 2.0
  cookies = 0
  best = 123456789012345.0
  
  while(True):
    time_to_finish = (goal - cookies) / speed
    best = min(best, elapsed + time_to_finish)
    time_to_buy = (cost - cookies) / speed
    if elapsed > best:
      break
    elapsed += time_to_buy
    speed += speed_bonus
    cookies = 0
    
  return best
  

for test in range(1, int(raw_input()) + 1):
  c, f, x = read_floats()
  sol = solve(c, f, x)
  print "Case #%d: %.7f" % (test, sol)

