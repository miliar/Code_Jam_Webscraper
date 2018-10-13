import sys

xxx = "welcome to code jam"

lookup = {}
for c in xxx:
  lookup[c] = set()
for i in xrange(0, len(xxx)):
  lookup[xxx[i]].add(xxx[0:i])

def Handle(line):
  prefixes = {}
  prefixes[""] = 1
  for i in xrange(0, len(xxx)):
    prefixes[xxx[:i+1]] = 0

  for c in line:
    ps = lookup.get(c)
    if ps == None:
      continue
    for p in ps:
      prefixes[p + c] += prefixes[p]
  return prefixes[xxx]

N = int(sys.stdin.readline().strip())

for i in xrange(0, N):
  line = sys.stdin.readline()[:-1]
  num = Handle(line)
  print "Case #%d: %04d" % (i + 1, num % 10000)
