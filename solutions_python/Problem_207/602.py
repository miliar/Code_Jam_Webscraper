import sys

def checkDone(stable):
  for s in stable:
    if s!=0:
      return False

  return True

def solve(stable):
  stableComposition = []
  stableColors = ['R', 'O', 'Y', 'G', 'B', 'V']

  for i in range(0, len(stable)):
    if stable[i] > 0:
      if stable[i] == max(stable):
        startingColor = i
        break;

  # for i in range(0, len(stable)):
  #   curColorCount = stable[i]
  #   nextColorCount = stable[ (i + 1) % len(stable)]

  #   if(curColorCount != 0 and nextColorCount != 0):
  #     startingColor = i;
  #     break;

  moveDone = True;


  while checkDone(stable) == False:

    stableComposition.append( stableColors[startingColor] )
    stable[startingColor] -= 1

    # print stable
    # print stableComposition
    # print startingColor
    # print [startingColor + 2, startingColor + len(stable) + 2]

    # Search next unicorn
    newStartingColor = startingColor

    index = -1
    tmpvalue = -1
    for i in range(startingColor + 2, startingColor + len(stable) - 1):

      if stable[i% len(stable)] > 0:
        if(stable[i% len(stable)])>=tmpvalue:
          index = i% len(stable);
          tmpvalue = stable[i% len(stable)]

      if sum(stable) == 2 :
        if stable[i% len(stable)] > 0:
          if stableColors[i% len(stable)] == stableComposition[0]:
            index = i% len(stable)
            break

    if(index == -1):
      break

    newStartingColor = index;
    
    if newStartingColor == startingColor:
      break

    startingColor = newStartingColor

  # print stableComposition

  if checkDone(stable) == False:
    return "IMPOSSIBLE"

  firstIndex = stableColors.index(stableComposition[0])
  lastIndex = stableColors.index(stableComposition[-1])

  if lastIndex == firstIndex or lastIndex == ((firstIndex + 1) % len(stable)) or firstIndex == ((lastIndex + 1) % len(stable)):
    return "IMPOSSIBLE"

  return "".join(stableComposition);

t = int(raw_input())
for i in range(1, t + 1):


  unicorns, red, orange, yellow, green, blue, violet = map(int,[s for s in raw_input().split(" ")])

  stable = [red, orange, yellow, green, blue, violet]

  result = solve(stable)
  
  # print result

  print("Case #{}: {}".format(i, result))
  sys.stdout.flush()