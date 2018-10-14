import copy
from scipy import argmax
def getBiggerSame(AA):
	A=copy.deepcopy(AA)
	N = len(A)
	if N<2:
		return False
	found=False
	j=N-2
	while True:
		G = [xx for xx in range(j+1,N) if (A[xx]>A[j])]
		if len(G)>0:
			ti = min(G,key=lambda xx:A[xx])
			#swap
			#except:
			#	print "type is ", type(A[j+1:])
			#	print "it is ",A[j+1:]
			#	raise TypeError
			t = A[ti];A[ti]=A[j];A[j]=t;
			A[j+1:] = sorted(A[j+1:])
			return A
		else:
			j=j-1
			if j<0:
				return False

def getBiggerDiff(A):
	AA = sorted([x for x in A if x!='0'])
	NZ = len(A)-len(AA)
	New = [AA[0]]
	New.extend(['0']*(NZ+1))
	New.extend(AA[1:])
	return New
def getNext(num):
	A = list(str(num))
	AA = getBiggerSame(A)
	if AA:
		return ''.join(AA)
	else:
		return ''.join(getBiggerDiff(A))

