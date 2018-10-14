import fileinput

class TestCase(object):
  def __init__(self, maxS, count):
    self.maxS = maxS
    self.count = count

def solve(t):

  userCount = 0
  needCount = 0
  shyLevel = 0
  for x in t.count:
    if x == 0:
      shyLevel = shyLevel + 1
      continue

    temp = 0
    if shyLevel > userCount:
      temp = (shyLevel - userCount)

    userCount = userCount + int(x) + temp
    needCount = needCount + temp
    shyLevel = shyLevel + 1
  return needCount

start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue
    
  data = [x for x in line.split()]
  #print data
  t = TestCase(int(data[0]), data[1])
  testCases.append(t)

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


