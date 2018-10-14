import math

f = open('A-large.in', 'r')
T = int(f.readline())
for testCase in range(1, T+1):
  N = int(f.readline())
  m = map(int, f.readline().split())

  # First method
  total = 0
  for i in range(N-1):
    drop = m[i] - m[i+1]
    if (drop > 0):
      total += drop
  first = total

  # Second method

  # Find biggest drop
  maxDrop = 0
  for i in range(N-1):
    drop = m[i] - m[i+1]
    if (drop > maxDrop):
      maxDrop = drop

  total = 0
  for i in range(N-1):
    if (m[i] < maxDrop):
      total += m[i]
    else:
      total += maxDrop

  second = total
  print "Case #%d: %d %d" % (testCase, first, second)


