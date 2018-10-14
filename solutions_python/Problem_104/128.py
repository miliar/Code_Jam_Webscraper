
def getit(S, k):
	L = []
	while(k!= -1):
		k1 = S[k]
		if(k1 == -1):
			L.append(k)
		else:
			L.append(k-k1)
		k = k1
	L.sort()
	return L
		

def process(L):
	L.sort()
	S = {}
	LL = [[L[i]] for  i in xrange(len(L))]
	
	for i in xrange(len(L)-1):
		if L[i] == L[i+1]:
			return [[L[i]], [L[i+1]]]
					
		S[L[i]] = -1
	
		
	for i in xrange(len(L)):
		for j in xrange(i):
			for k in LL[j]:
				key = k + L[i]
				if key in S:
					# found a match!					
					L1 = getit(S, key)
					L2 = getit(S, k)					
					L2.append(L[i])
					L2.sort()
					print L1, ': ', sum(L1)
					print L2, ': ', sum(L2)
					return [L1, L2]
				else:
					S[key] = k
					LL[i].append(key)
					
	return "Impossible"
			
	

def slst(lst):
	s = str(lst[0])
	for i in lst[1:]:
		s += ' ' + str(i)
	s += '\n'
	return s
	
def run():
	#fin = open('C-large.in', 'r')
	#fin = open('C-small-attempt0.in', 'r')
	fin = open('C-small-attempt0.in', 'r')
	L = [[int(i) for i in x.strip().split()] for x in fin.readlines()]
	fin.close()
	
	T = L[0][0]
	
	OL = []
	for i in xrange(1, T+1):
		OL.append('Case #' + str(i) + ':\n')
		opt = process(L[i][1:])
		if opt == 'Impossible':
			OL.append('Impossible\n')
		else:
			OL.append(slst(opt[0]))
			OL.append(slst(opt[1]))
	
	
	fout = open('C-small.out', 'w')
	fout.writelines(OL)
	fout.close()
		
run()
