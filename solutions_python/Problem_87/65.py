from __future__ import division

f = [l[:-1] for l in file("in")][1:]

case = 0
while len(f):
  case += 1
  nums = [int(x) for x in f.pop(0).split(" ")]
  length = int(nums.pop(0))
  speed = nums.pop(0)
  running = nums.pop(0)
  stamina = nums.pop(0)
  next_lines = nums.pop(0)
  walkways = []

  #start stop speed
  for x in range(next_lines):
    walkways.append([int(x) for x in f.pop(0).split(" ")])

  non_walkway_dist = length
  for walkway in walkways:
    non_walkway_dist -= walkway[1] - walkway[0]

  if non_walkway_dist > 0:
    walkways.append([0, non_walkway_dist, 0])

  total_time = 0
  for walkway in walkways:
    total_time += (walkway[1] - walkway[0])/(walkway[2] + speed)

  #figure out how much time we can save

  saved_time = []
  for walkway in walkways:
    dist = walkway[1] - walkway[0]
    spd = walkway[2]
    time_before = (dist)/(spd + speed) #walkway + yourspeed
    time_after = (dist)/(spd + running)
    #speed at which you gain time, amount of time saved, amount of time used
    saved_time.append(((time_before - time_after)/time_after, time_after, time_before - time_after))

  saved_time.sort(reverse=True,key = lambda x: x[0])

  for saved in saved_time:
    time_used = saved[1]
    if time_used < stamina:
      stamina -= time_used
      total_time -= saved[2]
    else:
      total_time -= saved[0] * stamina
      break


  print "Case #%d: %f" % (case, total_time)

