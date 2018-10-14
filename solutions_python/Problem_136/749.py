T = int(raw_input())
for t in range(1,T+1):
  print "Case #"+str(t)+":",
  C,F,X = map(float,raw_input().split())
  timeToLastFarm = 0
  cookieGen = 2
  endTimes = []
  for farms in range(1,1000000):
    endTimes.append(timeToLastFarm + X/cookieGen)
    timeToLastFarm += C / cookieGen
    cookieGen+=F
    if (endTimes[-1]>endTimes[0]):
      break
  print min(endTimes)

