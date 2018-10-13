from math import ceil

def calculateTotalFactories(c, f, x):
  rate = f*(x-c)/c
  # discount the constant 2 cookies we get from clicking.
  rate -= 2
  return max(int(ceil(rate/f)), 0)
  
def calculateTotalTime(c, f, x, n):
  time = 0
  for i in xrange(n):
    time += c/(2+(i*f))
  return time + x/(2+(n*f))

lines = open("input.txt").readlines()
outputLines = []
numTests = int(lines.pop(0))
for lineNumber in range(numTests):
  (c, f, x) = lines[lineNumber].split(' ')
  (c, f, x) = (float(c), float(f), float(x))
  time = calculateTotalTime(c, f, x, calculateTotalFactories(c, f, x))
  outputLines.append("Case #%d: %s\n" % (lineNumber+1, repr(time)))

fp = open("output.txt", "w")
fp.writelines(outputLines)
fp.close()
