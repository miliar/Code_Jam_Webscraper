import sys
import fileinput

numTestCases = None
testCase = 0

def flipper(char):
  if (char == '+'):
    return '-'
  if (char == '-'):
    return '+'
  return None

def flipnrecur(pancakes, k, numFlips):
  global flipDict
  #base case:
  #pancakes have all been flipped, return num of flips
  if (pancakes == ''.join('+' for i in range(len(pancakes)))):
    return numFlips

  minFlips = sys.maxsize

  #For every index between 0 and num of pancakes minus k
  for x in range(0, len(pancakes) - (k - 1)):

    #create the flipped string for the approprate range
    intermediate = ''.join([flipper(j) for j in pancakes[x:x+k]])

    #if a set of k '+' were flipped, don't recur
    if (intermediate == ''.join('-' for j in range(k))):
      continue

    flipped = pancakes[0:x]+intermediate+pancakes[x+k:]

    if flipped in flipDict:
      if (numFlips + 1) < flipDict[flipped]:
        flipDict[flipped] = numFlips + 1
      else:
        continue
    else:
      flipDict[flipped] = numFlips + 1

    # recur with the flipped result, and an incremented number of flips
    recurredNumFlips = flipnrecur(flipped, k, numFlips + 1)

    #If the recurred result is less than the curr value of minFlips, store it
    if recurredNumFlips < minFlips:
      minFlips = recurredNumFlips


  return minFlips

for line in fileinput.input():
  if fileinput.isfirstline():
    numTestCases = int(line.rstrip())
    continue
  testCase += 1
  [test, k] = line.split(' ')
  flipDict = {}
  numFlips = flipnrecur(test, int(k), 0)
  if numFlips == sys.maxsize:
    numFlips = "IMPOSSIBLE"
  print "Case #"+str(testCase)+": "+str(numFlips)


