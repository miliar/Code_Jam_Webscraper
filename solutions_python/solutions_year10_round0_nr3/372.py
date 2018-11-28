from sys import stdin

def next(i, N):
  res = i + 1
  if res == N:
    res = 0
  return res

def prev(i, N):
  if i == 0:
    return N - 1
  return i - 1

TTT = int(stdin.readline())
for ttt in range(1,TTT+1):
  R, K, N = map(int,stdin.readline().split())
  g = map(int,stdin.readline().split())
  #print R, K, N, g
  totalPeople = reduce(lambda x, y: x+y,  g)
  if totalPeople <= K:
    print "Case #%d: %d" % (ttt,R*totalPeople)
    continue

  cash = []
  curGroup = 0
  startIndexes = []
  while R:
    curCash = 0
    curRiders = 0
    startIndex = curGroup
    if startIndex in startIndexes:
      loopStart = startIndexes.index(startIndex)
      loop = cash[loopStart:]
      remLoops = int(R/len(loop))
      loopCash = reduce(lambda x, y: x+y,  loop)
      fullCash = loopCash*remLoops + reduce(lambda x, y: x+y,  cash)
      R = R % len(loop)
      index = 0
      while R:
        fullCash = fullCash + loop[index]
        index = index + 1
        R = R -1
      print "Case #%d: %d" % (ttt,fullCash)
      break
    else:
      startIndexes.append(startIndex)
    while curRiders < K:
      if curRiders + g[curGroup] <= K:
        curRiders = curRiders + g[curGroup]
      else:
        break
      curGroup = next(curGroup, N)
    R = R - 1
    cash.append(curRiders)
    if R == 0:
      print "Case #%d: %d" % (ttt, reduce(lambda x, y: x+y,  cash))

    #print curGroup, cash
  #print cash
  #print startIndexes

      
    
      
    
    
