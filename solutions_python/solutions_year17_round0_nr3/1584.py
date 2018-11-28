############
# BATHROOM #
############

import math

def spaces(n, k):
  wave = int(math.log(k, 2))
  freeSpaces = n - (2 ** wave - 1)
  peopleInWave = 2 ** wave
  guarantee = freeSpaces // peopleInWave
  kPositionInWave = k - 2 ** wave
  kSpaces = guarantee + int(kPositionInWave < (freeSpaces % peopleInWave))
  maxSize = kSpaces // 2
  minSize = maxSize if kSpaces % 2 == 1 else maxSize - 1
  return (maxSize, minSize)

def main(tests):
  file = open("bathroom_output.txt", "w")
  for i in range(len(tests)):
    sol = spaces(tests[i][0], tests[i][1])
    file.write("Case #" + str(i + 1) + ": " + str(sol[0]) + " " + str(sol[1]) + "\n")
  file.close()

def getInput():
  with open("C-small-2-attempt0.in") as f:
    lines = f.readlines()
    cases = int(lines[0][:-1])
    tests = []
    for i in range(1, cases + 1):
      tests.append(map(lambda x: int(x), lines[i].split()))
  return tests

main(getInput())