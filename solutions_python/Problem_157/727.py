import sys

trace = False

I = 2
J = 3
K = 4

P = [0, 1, I, J, K]

NI = -2
NJ = -3
NK = -4

N = [0, -1, NI, NJ, NK]

def trace(string):
	if(trace):
		print string

def runQTest():
	assert(q(1, 1) == 1)
	
	assert(q(-I, -K) == -J)
	assert(q(-I, -K) == NJ)
	assert(q(I, -K) == J)
	
	
	
	assert(q(I, I) == -1)
	assert(q(I, J) == K)
	assert(q(I, K) == NJ)
	
	assert(q(J, I) == NK)
	assert(q(J, J) == -1)
	assert(q(J, K) == I)
	
	assert(q(K, I) == J)
	assert(q(K, J) == NI)
	assert(q(K, K) == -1)
	
	
	## negative result sign test
	assert(q(I, I) == -1)
	assert(q(I, J) == K)
	assert(q(I, K) == -J)
	
	assert(q(J, I) == -K)
	assert(q(J, J) == -1)
	assert(q(J, K) == I)
	
	assert(q(K, I) == J)
	assert(q(K, J) == -I)
	assert(q(K, K) == -1)
	
	
	# negative first input
	assert(q(-I, I) == 1)
	assert(q(-I, J) == NK)
	assert(q(-I, K) == J)
	
	assert(q(-J, I) == K)
	assert(q(-J, J) == 1)
	assert(q(-J, K) == NI)
	
	assert(q(-K, I) == NJ)
	assert(q(-K, J) == I)
	assert(q(-K, K) == 1)
	
	# negative second input
	assert(q(I, -I) == 1)
	assert(q(I, -J) == NK)
	assert(q(I, -K) == J)
	
	assert(q(J, -I) == K)
	assert(q(J, -J) == 1)
	assert(q(J, -K) == NI)
	
	assert(q(K, -I) == NJ)
	assert(q(K, -J) == I)
	assert(q(K, -K) == 1)
	
	# both negative
	assert(q(-I, -I) == q(I, I))
	assert(q(-I, -J) == q(I, J))
	assert(q(-I, -K) == q(I, K))
	
	assert(q(-J, -I) == q(J, I))
	assert(q(-J, -J) == q(J, J))
	assert(q(-J, -K) == q(J, K))
	
	assert(q(-K, -I) == q(K, I))
	assert(q(-K, -J) == q(K, J))
	assert(q(-K, -K) == q(K, K))
	
	trace('"Ran Testing!"');
	

def q(a, b):
	
	res = False
	negative = False
	
	if (a in N and b in N):
		a = P[-a]
		b = P[-b]
		
	elif (a in N):
		a = P[-a]
		negative = True
		
	elif (b in N):
		b = P[-b]
		negative = True

	if (a == 1 and b == 1): res = 1
	elif (a == b): res = -1
	
	
	elif(a == 1): res = b
	elif(b == 1): res = abs
	
	
	elif(a == I and b == J): res = K
	elif(a == I and b == K): res = NJ
	
	elif(a == J and b == I): res = NK
	elif(a == J and b == K): res = I
	
	elif(a == K and b == I): res = J
	elif(a == K and b == J): res = NI
	
	if(res == False):
		print(a,b)
		assert(res)
	
	if(negative):
		if(res in P):
			return N[res]
		elif(res in N):
			return P[-res]
			
	return res

def valueQ(string):
	if(string == 'I'): return I
	elif(string == 'J'): return J
	elif(string =='K'): return K
	
def keyQ(val):
	if(val == I): return 'I'
	elif(val == J): return 'J'
	elif(val == K): return 'K'
	
		
def reduce(string, length, val):
	string = string.strip()
	if(length < 1):
		return False
	string = list(string)
	
	res = valueQ(string[0])
	
	if(length == 1):
		if(res == val):	
			return True
		else:
			return False
	
	for i in xrange(length-1):
		res = q(res, valueQ(string[i+1]))
		
	if(res == val): 
		return True
	else:
		return False
	
def findKHelp(string, length):

	if(length < 1): 
		return False

	if(reduce(string, length, K)):
		return True
		
	return False
	
def findJKHelp(string, length):

	if(length < 2): 
		return False

	s = list(string)

	lastJ = valueQ(s[0])
	
	if(lastJ == J):
		return findKHelp(string[1: length], length-1)
	
	for i in xrange(length-1):
		isJ = lastJ = q(lastJ, valueQ(s[i+1]))
		if(isJ == J):
			return findKHelp(string[i+2:length], length-(i+2))	
		
	return False	
	
def findIJKHelp(string, length):

	if(length < 3): 
		return False	
	
	s = list(string)

	lastI = valueQ(s[0])
	
	if(lastI == I):
		return findJKHelp(string[1: length], length-1)
	
	for i in xrange(length-1):
		isI = lastI = q(lastI, valueQ(s[i+1]))
		if(isI == I):
			return findJKHelp(string[i+2:length], length-(i+2))
	
	return False
	
def findIJK(L, X, string):

	length = L*X

	return findIJKHelp(string, length)
			
if __name__ == '__main__':

	testing = False

	if (len(sys.argv) < 2):
		testing = True
		runQTest()
		f = open('testc', 'r')

	else: 
		filename = sys.argv[1]
		f = open(filename, 'r')

	testCases = int(f.next())
	caseNum = 0
	cases = []

	for i in xrange(testCases):
		caseNum += 1
		l1 = f.next().split()
		l2 = f.next().rstrip()
		
		
		L = int(l1[0])
		X = int(l1[1])
		l2 = (l2*X).upper().rstrip()
		
		TorF = findIJK(L, X, l2)
		
		if(TorF):
			string = 'YES'
		else:
			string = 'NO'
				
		print('Case #%s: %s' % (caseNum, string))
		
	
