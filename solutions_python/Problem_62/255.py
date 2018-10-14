#import cloud #PiCloud open source library
#cloud.start_simulator() #local

def doCase(n):
  wires = []
  for _ in xrange(n):
	ab = stdin.readline()
	a, b = ab.split()
	wires.append((int(a), int(b)))
  inter = 0
  for ai, bi in wires:
	for aj, bj in wires:
	  if (bj > bi and ai > aj) or (bj < bi and ai < aj):
		inter+=1
  return inter/2
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  f = stdin.readline()
  n = int(f)
  val = doCase(n)
  print 'Case #%s: %s' % (1+i, val)