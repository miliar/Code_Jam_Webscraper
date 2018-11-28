PROBS = {}
def calcKey(A,B,C,i,n,s):
	global PROBS
	n += 1
	if n >= len(C):
		PROBS[s] = i
		return
	calcKey(A,B,C,i*C[n],n,s+'R')
	calcKey(A,B,C,i*(1-C[n]),n,s+'X')
		
	
with file('A-small-attempt0.in.txt') as f:
	T = int(f.readline())
	fo = open('output.txt','w')
	for xj in range(1,T+1):
		PROBS = {}
		expected = []
		x = f.readline().strip().split()
		A = int(x[0])
		B = int(x[1])
		C = [float(x) for x in f.readline().strip().split()]
		calcKey(A,B,C,C[0],0,'R')
		calcKey(A,B,C,(1-C[0]),0,'X')
		
		print PROBS
		ik = 0
		for x in PROBS.keys():
			if 'X' not in x:
				ik += PROBS[x] * ((B-A)+1)
			else:
				ik += PROBS[x] * ((B-A)+2+B)
		expected.append(ik)
		
		for n in range(1,A+1):
			ik = 0
			for x in PROBS.keys():
				if 'X' not in x[:-n]:
					ik += PROBS[x] * (n+(B-(A-n))+1)
				else:
					ik += PROBS[x] * (n+(B-(A-n))+2+(B))
			expected.append(ik)
		
		expected.append(2+B)
		fo.write('Case #%i: %f\n'%(xj, min(expected)))
