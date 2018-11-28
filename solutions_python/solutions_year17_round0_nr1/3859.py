def flip(cakes):

  for cnt in range(len(cakes)):
    if cakes[cnt] == '+':
      cakes = cakes[:cnt] + "-" + cakes[cnt+1:]
    else:
      cakes = cakes[:cnt] + "+" + cakes[cnt+1:]
  return cakes

def minflips(pancakes, flipperSize):

  lengthofOven = len(pancakes)
  if '-' not in pancakes:
    return 0

  if lengthofOven < flipperSize:
    return -1

  if ('+' not in pancakes) and ((lengthofOven % flipperSize) == 0):
    return lengthofOven // flipperSize

  start = 0
  end = start+flipperSize-1
  flipCnt = 0
  while end < lengthofOven:
    if pancakes[start] == '+':
      start+= 1
      end = start+flipperSize-1
    else:
      if end <=lengthofOven:
        pancakes = pancakes[:start] + flip(pancakes[start:end+1]) + pancakes[end+1:]
        flipCnt += 1

  if not ('-' in pancakes):
	  return flipCnt
  return -1


tests = []
t = int(input().strip())

for i in range(1, t + 1):
  tests.append([s for s in input().split(" ")])  # read a list of integers, 2 in this case

for num in range(t):
  pancakes = tests[num][0]
  flipperSize = int(tests[num][1])
  minCnt = minflips(pancakes, flipperSize)
  
  if minCnt == -1:
    print ("Case #{0}: IMPOSSIBLE".format(num+1))
  else:
    print ("Case #{0}: {1}".format(num+1, minCnt))

