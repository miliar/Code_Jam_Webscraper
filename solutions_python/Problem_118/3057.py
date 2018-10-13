import sys
import math

def numberIsPal(number):
  if str(number) == str(number)[::-1]:
    return True

numLines = sys.stdin.readline()

cases = []
results = [0] * int(numLines)

for i in range(int(numLines)):
  case = sys.stdin.readline().strip()
  cases.append(case.split(' '))

numCase = 0
for case in cases:
  for num in range(int(math.ceil(math.sqrt(float(case[0])))), int(math.floor(math.sqrt(float(case[1])))) + 1):
    if numberIsPal(num) and numberIsPal(num*num):
      results[numCase] = results[numCase] + 1
  numCase += 1

for resultNum in range(len(results)):
  print "Case #" + str(resultNum + 1) + ": " + str(results[resultNum])
