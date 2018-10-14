QMul = [[0, 1, 2, 3, 4, 5, 6, 7], [1, 4, 3, 6, 5, 0, 7, 2], [2, 7, 4, 1, 6, 3, 0, 5], [3, 2, 5, 4, 7, 6, 1, 0], [4, 5, 6, 7, 0, 1, 2, 3], [5, 0, 7, 2, 1, 4, 3, 6], [6, 3, 0, 5, 2, 7, 4, 1], [7, 6, 1, 0, 3, 2, 5, 4]]
lookup = {"-1": 4, "-i": 5, "-j": 6, "-k": 7, "1": 0, "i": 1, "j": 2, "k": 3}

def cumProdList(L):
	global QMul
	Y = [0 for i in xrange(len(L))]
	Y[0] = L[0]
	for i in xrange(1,len(L)):
		Y[i] = QMul[Y[i-1]][L[i]]
	return Y

def solve_bruteForce(S, X):
	L = [1 if ch == "i" else (2 if ch == "j" else 3) for ch in S*X]
	cL = cumProdList(L)
	prodL = cL[-1]
	if prodL != lookup["-1"]:
		return "NO"
	iOccurred = False
	for q in cL:
		if q == 1:
			iOccurred = True
		if iOccurred and q == 3:
			return "YES"
	return "NO"

def solve_case(S, X):
	global lookup
	L = [1 if ch == "i" else (2 if ch == "j" else 3) for ch in S]
	cL = cumProdList(L)
	prodL = cL[-1]
	if prodL == lookup["1"]:
		return "NO"
	elif prodL == lookup["-1"]:
		if X%2==0:
			return "NO"
	elif X%4 != 2:
		return "NO" # prod is I, J, K, -I, -J or -K and num repeats is not 2 mod 4
		
	# Control reaches here means the total product is correct
	iOccurred = False
	
	p = lookup["1"]
	for k in xrange(1, 9):
		if X >= k:
			cL2 = [QMul[p][x] for x in cL]
			for q in cL2:
				if q == 1:
					iOccurred = True
				if iOccurred and q == 3:
					return "YES"
			p = QMul[p][prodL]
			
	return "NO"


def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [x.strip() for x in fin.readlines()]
	fin.close()	
	out = []	
	T = int(L[0])
	k = 1
	for i in xrange(T):
		X = map(int, L[k].split())[1]
		k+=1 
		S = L[k]
		k+=1				
		out.append('Case #' + str(i+1) + ': '+ str(solve_case(S, X))+ "\n")
	fout = open(out_name, 'w')
	fout.writelines(out)
	fout.close()
	
	return

#sys.setrecursionlimit(1000)	
#solve('C-small-attempt0.in', 'C-small-attempt0.out')
#solve('C-small-attempt1.in', 'C-small-attempt1.out')
solve('C-large.in', 'C-large.out')

#solve('C-test.in', 'C-test.out')
