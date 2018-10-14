import sys

inputFile = sys.stdin
count = int(inputFile.readline())

lineno = 1
for line in inputFile:
  if (lineno % 2) == 1:
    lineno += 1
    continue

  row = line.split()
  row = map(int, row)
  row.sort()

  total = reduce(lambda a, b: a ^ b, row)
  
  if total == 0:
    row.reverse()
    row.pop()
    total = reduce(lambda a, b: a + b, row)
  else:
    total = "NO"

  print "Case #%d:" % (lineno/2),

  print total
  
  lineno += 1
