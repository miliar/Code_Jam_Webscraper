#!/usr/bin/python


def getMinTime(c, f, x):
  seconds = 0.0
  rate = 2.0
  secsToNextFarm = c / rate
  secsToTarget = x / rate
  if secsToTarget < secsToNextFarm:
    return secsToTarget

  bestTime = secsToTarget

  while True:
    seconds += secsToNextFarm
    rate += f
    secsToNextFarm = c / rate
    secsToTarget = x / rate
    if (secsToTarget + seconds) < bestTime:
      bestTime = secsToTarget + seconds 
    else:
      break
  return bestTime


def readfile(filepath):
  with open(filepath, 'r') as f:
    for line in f:
      yield line.rstrip()


lines = readfile('smallInput.txt')
cases = None
current_case = 1

for line in lines:
  if cases is None:
    cases = int(line)
    continue
  [c, f, x] = [float(i) for i in line.split(' ')]
  print "Case #%d: %.7f" % (current_case, getMinTime(c, f, x))
  current_case += 1

