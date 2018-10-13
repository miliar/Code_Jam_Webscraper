# REASON NUMBER TWO WHY CIVILIZATIONS DIE:
# MANY SOFTWARE ENGINEERS ARE TRAINED TO
# IMPLEMENT AND SUBMIT SOLUTIONS WITHIN 2.5
# HOURS, BELIEVING THE SOLUTIONS ARE BUG-FREE

import sys
inp = sys.stdin
T = int(inp.readline())

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def read_floats():
	return [float(x) for x in raw_input().strip().split()]

NaosBlocks = []
KensBlocks = []
N = 0

def KenChoose(NC):  # what Ken would choose given Naomi's choice
	if NC > KensBlocks[N-1]:  return 0
	i = 0
	for k in KensBlocks:
		if k > NC:  return i
		i+=1
	print 'Error in KenChoose() !'
	return -1
	
for t in range(1, T+1):
	print 'Case #' + str(t) + ':',
	N = int(raw_input())
	NaosBlocks = read_floats()
	KensBlocks = read_floats()
	NaosBlocks.sort()
	KensBlocks.sort()
	nsW = nsDW = 0
	N2 = N
	NaosBlocks2 = NaosBlocks[:]
	KensBlocks2 = KensBlocks[:]
	while N:
		nc = N-1
		kc = KenChoose(NaosBlocks[nc])
		if NaosBlocks[nc] > KensBlocks[kc]:  nsW += 1
		NaosBlocks.pop(nc)
		KensBlocks.pop(kc)
		N-=1
	skip = 0
	while N2:
		yes=0
		for i in range(skip, N2):
			if NaosBlocks2[i] > KensBlocks2[0]:
				NaosBlocks2.pop(i)
				KensBlocks2.pop(0)
				nsDW += 1
				skip = i
				yes=1
				break
		if yes==0:	break
		N2-=1
	print nsDW, nsW
