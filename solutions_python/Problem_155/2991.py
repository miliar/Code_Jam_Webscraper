T = int(raw_input())
ShynessCount = []
for tc in xrange(T):
  SMaxStr, Shyness = raw_input().strip().split()
  SMax = int(SMaxStr)
  ShynessCount = map(int, list(Shyness))
  friends = 0
  runningTotal = 0
  friends = 0
  for i,s in enumerate(ShynessCount):
    friendsAdded = 0
    if runningTotal < i:
      friendsAdded = (i-runningTotal)
      friends += friendsAdded
    runningTotal += friendsAdded
    runningTotal += s
  print "Case #%d: %d" % (tc+1, friends)
    
  
