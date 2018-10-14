import sys

def solve(goal, horses, times):
  annieSpeed = 0;

  maxTime = max(times)

  annieSpeed = goal / maxTime

  return annieSpeed

t = int(raw_input())
for i in range(1, t + 1):

  horses = list()
  times = list()

  goal, numHorses = map(float,[s for s in raw_input().split(" ")])

  numHorses = int(numHorses)

  for h in range(numHorses):
    position, speed = map(float,[s for s in raw_input().split(" ")])

    horse = dict()
    horse['position'] = position
    horse['speed'] = speed
    horse['time'] = (goal - position) / speed

    horses.append(horse)
    times.append(horse['time'])


  result = solve(goal, horses, times)
  
  # print result

  print("Case #{}: {}".format(i, result))
  sys.stdout.flush()