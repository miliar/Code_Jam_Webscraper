# REASON NUMBER TWO WHY CIVILIZATIONS DIE:
# MANY SOFTWARE ENGINEERS ARE TRAINED TO
# IMPLEMENT AND SUBMIT SOLUTIONS WITHIN 2.5
# HOURS, BELIEVING THE SOLUTIONS ARE BUG-FREE

import sys
inp = sys.stdin
T = int(inp.readline())

def readbins():
	return [int('0b'+x,2) for x in raw_input().strip().split()]
def readints():
	return [int(x) for x in raw_input().strip().split()]
def readstrs():
	return [str(x) for x in raw_input().strip().split()]
def readfloats():
	return [float(x) for x in raw_input().strip().split()]
def countbits(x):
	res=0
	while x:
		res+=x&1
		x>>=1
	return res

for t in range(1, T+1):
  print 'Case #'+str(t)+':',
  A,B,K = readints()
  res=0
  for a in range(A):
	for b in range(B):
		if (a&b)<K: res+=1
  print res
