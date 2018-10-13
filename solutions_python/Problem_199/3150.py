pancakes = ''

def CanDoFlip(index, n):
  if (index + n) > len(pancakes):
    return False
  return True

def doFlip(index, n):
  global pancakes

  flipped = pancakes[:index]
  for p in pancakes[index:index+n]:
    if p == '+':
      flipped += '-'
    else:
      flipped += '+'
  flipped += pancakes[index+n:]
  pancakes = flipped

def flipBlanksInARow(k):
  global pancakes

  count = 0

  while '-'*k in pancakes:
    index = pancakes.index('-'*k)
    if CanDoFlip(index, k):
      doFlip(index, k)
      count += 1

  return count


def isAllHappy():
  return '-' not in pancakes

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  pancakes, k = [s for s in raw_input().split(" ")]
  k = int(k)

  count = 0
  allFlipsDone = False

  while not isAllHappy():
    count += flipBlanksInARow(k)
    if allFlipsDone:
      count = 'IMPOSSIBLE'
      break
    for j in range(len(pancakes)):
      if pancakes[j] == '-':
        if CanDoFlip(j, k):
          doFlip(j, k)
          count += 1
          break
      if j == len(pancakes) - 1:
        allFlipsDone = True


  print "Case #{}: {}".format(i, count)
