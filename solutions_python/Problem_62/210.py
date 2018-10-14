import itertools
from math import *

global l

print ''
f = "mytest"
f = "A-small-attempt0"
f = "A-large"
infile = open(f+".in", "r")
outfile = open(f+".out", "w")

def ReadData(foo):
  return list(map(foo, infile.readline().strip().split(" ")))
    
T = ReadData(int)[0]
for each in range (1, T+1):
  N = ReadData(int)[0]
  a = []
  b = []
  for i in range(N):
    (ai, bi) = ReadData(int)
    a.append(ai)
    b.append(bi)

  count = 0
  #print N, a, b
  if N > 1:
    for (i, j) in itertools.combinations(range(N), 2):
      if (a[i]-a[j])*(b[i]-b[j]) < 0:
        count += 1
        
  print 'Case #%d: %s\n' % (each, count)
  outfile.write('Case #%d: %s\n' % (each, count))
