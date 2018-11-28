import sys
from collections import deque

def canflip(cakes, flipsize, index):
  return (flipsize + index) <= len(cakes)

def flip(cakes, flipsize, index):
  for i in range(flipsize):
    cakes[index + i] *= -1
  return cakes
 
def done(cakes):
  return sum(cakes) == -1 * len(cakes)

def flipdone(cakes, flipsize, index):
  for i in range(index, index + flipsize):
    if cakes[i] > 0:
      return False
  return True

def output(result, casenum):
  print(f"Case #{str(casenum)}: {'IMPOSSIBLE' if result < 0 else str(result)}")

def str2arr(cakestring):
  return [ord(x) - 44 for x in list(cakestring)]
  
def str2tup(cakestring):
  return tuple(ord(x) - 44 for x in list(cakestring))

def arr2str(cakes):
  return "".join([chr(x + 44) for x in cakes])

def children(cakes, flipsize):
  flipped = []
  for i in range(len(cakes)):
    if canflip(cakes, flipsize, i):
      if not flipdone(cakes, flipsize, i):
        flipped.append(flip(list(cakes), flipsize, i))
  return flipped

def bfs(cakes, flipsize):
  visited = set()
  visited.add(tuple(cakes))
  q = deque()
  q.append([cakes, 0])
  while q:
    testnode = q.popleft()
    testcakes = testnode[0]
    counter = testnode[1]
    if done(testcakes):
      return counter
    for node in children(testcakes, flipsize):
      if not tuple(node) in visited:
        visited.add(tuple(node))
        q.append([node, counter + 1])
  return -1

f = open(sys.argv[1], 'r')
lines = int(f.readline())
for i in range(lines):
  [cakestring, flipsize] = f.readline().split()
  flipcount = 0
  if not done(str2tup(cakestring)):
    flipcount = bfs(str2arr(cakestring), int(flipsize))
  output(flipcount, i + 1)