from bisect import bisect_left

def timeMatrix(nVal, nSplit):
	# Builds an 1+nValx1+nSplit matrix T where T[a][b] is the lowest total using b splits starting at a
	T = [[1 for i in xrange(nSplit+1)] for j in xrange(nVal+1)] 
	for v in xrange(nVal+1):
		T[v][0] = v
	for s in xrange(nSplit+1):
		T[0][s] = 0
 
	for v in xrange(1, nVal+1):
		for s in xrange(1, nSplit+1):
			T[v][s] = v
			for vp in xrange(1, 1+v//2):
				for sp in xrange(0, s):
					test = max(T[vp][sp], T[v-vp][s-sp-1])
					if test < T[v][s]:
						T[v][s] = test
	return T
				
def mintime(D):
	D.sort()	
	mD = D[-1]
	
	bestScore = mD
	splits = 0
	vsplit = [[D[i], D[i], 0] for i in xrange(len(D))]
	vsplit.sort()
	for nsplits in xrange(mD):
		vsplit[-1][2] += 1
		A = vsplit[-1][1]
		B = vsplit[-1][2]+1
		vsplit[-1][0] = (A+ ((-A)%B))//B
		vsplit.sort()
		splits += 1
		if splits + vsplit[-1][0] < bestScore:
			bestScore = splits + vsplit[-1][0]
		
	return bestScore

def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [mintime(sorted(map(int, x.strip().split()))) for x in fin.readlines()[2::2]]
	fin.close()
	
	fout = open(out_name, 'w')
	fout.writelines(['Case #' + str(i+1) + ': ' + str(L[i]) + '\n' for i in xrange(len(L))])
	fout.close()
	
	return
	
#solve('B-small-attempt0.in', 'B-small-attempt0.out')
#solve('B-small-attempt1.in', 'B-small-attempt1.out')
#solve('B-small-attempt2.in', 'B-small-attempt2_thing.out')
#solve('B-small-attempt6.in', 'B-small-attempt6fosho.out')
solve('B-large.in', 'B-large.out')

#solve('B-test.in', 'B-test.out')
