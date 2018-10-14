#!/usr/bin/env python

def solve(steps):
  opos = 1
  bpos = 1
  count = 0
  osteps = [step for step in steps if step[0] == 'O']
  bsteps = [step for step in steps if step[0] == 'B']
  while len(steps):
    count += 1
    bmove = False
    omove = False
    if steps[0][0] == 'O' and opos == steps[0][1]:
        steps = steps[1:]
        osteps = osteps[1:]
        omove = True
    elif steps[0][0] == 'B' and bpos == steps[0][1]:
        steps = steps[1:]
        bsteps = bsteps[1:]
        bmove = True
    if len(osteps) > 0 and not omove:
      if opos > osteps[0][1]:
        opos -= 1
      elif opos < osteps[0][1]:
        opos += 1
    if len(bsteps) > 0 and not bmove:
      if bpos > bsteps[0][1]:
        bpos -= 1
      elif bpos < bsteps[0][1]:
        bpos += 1
    
  print(count)

if __name__ == "__main__":
  import sys
  inputFile = file(sys.argv[1], 'r')
  T = int(inputFile.readline())
  testCases = [line.split() for line in inputFile.readlines()]
  inputFile.close()

  for i in range(0, T):
    sys.stdout.write('Case #%d: ' % (i+1))
    N = int(testCases[i][0])
    testCase = [(testCases[i][j], int(testCases[i][j+1])) for j in range(1,N*2,2)]
    solve(testCase)
