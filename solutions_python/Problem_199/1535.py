###########
# PANCAKE #
###########

import sys
sys.setrecursionlimit(100000)

def flip(pancakes, size, start):
  for i in range(start, start  + size):
    pancakes[i] = not pancakes[i]

# -1 if impossible
def flipCount(pancakes, size):
  for i in range(len(pancakes)):
    if not pancakes[i]:
      if (i > len(pancakes) - size):
        return -1
      flip(pancakes, size, i)
      recFlipCount = flipCount(pancakes, size)
      return -1 if (recFlipCount == -1) else recFlipCount + 1
  return 0

def flipMain(tests):
  file = open("pancake_output.txt", "w")
  for i in range(len(tests)):
    sol = flipCount(tests[i][0], tests[i][1])
    if sol == -1:
      sol = "IMPOSSIBLE"
    file.write("Case #" + str(i + 1) + ": " + str(sol) + "\n")
  file.close()

def getFlipInput():
  with open("A-large.in") as f:
    lines = f.readlines()
    cases = int(lines[0][:-1])
    tests = []
    for i in range(1, cases + 1):
      line = lines[i]
      pancakes = []
      for j in range(len(line)):
        if line[j] == "-":
          pancakes.append(False)
        elif line[j] == "+":
          pancakes.append(True)
        elif line[j] == " ":
          size = int(line[j + 1 : -1])
      tests.append((pancakes, size))
  return tests

flipMain(getFlipInput())




