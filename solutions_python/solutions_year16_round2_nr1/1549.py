import itertools

def a(S):
	D = dict()
	D[0] = (4,list("ZERO"))
	D[1] = (3, list("ONE"))
	D[2] = (3, list("TWO"))
	D[3] = (5, list("THREE"))
	D[4] = (4, list("FOUR"))
	D[5] = (4, list("FIVE"))
	D[6] = (3, list("SIX"))
	D[7] = (5, list("SEVEN"))
	D[8] = (5, list("EIGHT"))
	D[9] = (4, list("NINE"))
	n = len(S)
	pos = []
	for i in range(7):
		for j in range(10):
			for k in range(4):
				if i*3 + j*4 + k*5 == n:
					pos.append((i,j,k))
	A = [D[i][1] for i in range(10) if len(D[i][1]) == 3]
	B = [D[i][1] for i in range(10) if len(D[i][1]) == 4]		
	C = [D[i][1] for i in range(10) if len(D[i][1]) == 5]
	
	for k in pos:
		for m in list(itertools.combinations_with_replacement(range(10), sum(k))):
			cand = []
			band = []
			for j in m:
				cand.append(D[j][1])
				band.append(j)
			if sorted(itertools.chain.from_iterable(cand)) == sorted(S):
				return ("").join([str(x) for x in band])


t = int(raw_input())
for i in xrange(1, t + 1):
  A = list(raw_input())
  print "Case #{}: {}".format(i, a(A))
 
