import sys

inputFile = sys.stdin
count = int(inputFile.readline())

def gcd(a,b):
  while b > 0: a,b = b, a%b
  return a

lineno = 1
for line in inputFile:
  row = line.split()
  n, events = int(row[0]), map(int, row[1:])
  diffs = []
  for t in xrange(1, len(events)):
    d = events[t] - events[t-1]
    if d < 0: d *= -1
    if d > 0:
      diffs.append(d)

  g = diffs[0]
  for d in diffs:
    g = gcd(g, d)

  if g < 0: g *= -1
 
  print "Case #%d:" % lineno,
  if events[0] % g == 0:
    print 0
  else:
    print g - (events[0] % g)

  lineno += 1

