import fileinput

class TestCase(object):
  def __init__(self, num, dinerP):
    self.numberOfDiner = num
    self.dinerP = dinerP


def sortPancakes(t):

  waitTime = 1
  maxP = 0
  for x in range (0, t.numberOfDiner):
    p = int(t.dinerP[x])
    if (p > maxP):
      maxP = p

  minTime = maxP
  if minTime <= waitTime:
    return minTime

  for x in range (1, maxP):
    waitTime = x
    distributeTime = 0
    for x in range (0, t.numberOfDiner):
      p = int(t.dinerP[x])
      #print "waitTime : " + str(waitTime) + " dis " + str(distributeTime)
      #print "p is " + str(p)
      if (p > waitTime):
        
        distributeTime = distributeTime + (p - waitTime) / waitTime 
        if ((p - waitTime) % waitTime) != 0:
          distributeTime = distributeTime +1

    total = distributeTime + waitTime
    #print "wait time " + str(waitTime) + " total " + str(total) + " dis " + str(distributeTime)
    if minTime > total:
      minTime = total

  return minTime

start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue

  if (i % 2) == 0:
    t = TestCase(int(line), [])
    testCases.append(t)
  else:
    testCases[ i /2].dinerP = [int(x) for x in line.split()]

  i = i + 1

i = 1

f = open('answer', 'w')

for t in testCases:
  answer = sortPancakes(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


