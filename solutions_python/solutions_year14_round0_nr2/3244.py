"""
Solves cookie clicker problem.
"""

def out(case, num):
  print "Case #%d: %.7f" % (case+1, num)

inFile = [line.rstrip() for line in open('input.txt')]
T = int(inFile.pop(0))

for case in range(T):
  line = inFile[case].split()
  CPS = 2.0
  seconds = 0.0
  C = float(line[0])
  F = float(line[1])
  X = float(line[2])

  for coef in range(100000):
    if (X / CPS) + seconds > X / (CPS + F) + (seconds + (C / CPS)):
      seconds += C / CPS
      CPS += F
    else:
      seconds += X / CPS
      break

  out(case, seconds)
