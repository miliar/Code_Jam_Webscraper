from fractions import gcd
from sys import stdin, stdout
trials = stdin.readline()
for i, line in enumerate(stdin.readlines()):
  events = map(int, line.split())[1:]
  events.sort()
  T = reduce(gcd, (e - events[0] for e in events), 0)
  stdout.write('Case #%s: %s\n' % (i+1, (T-events[0])%T))