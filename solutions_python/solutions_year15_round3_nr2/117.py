import itertools

def joinTuple(A):
	ans = ''
	for each in A:
		ans += str(each)
	return ans	

def getAll(str, times):	
	return [p for p in itertools.product(list(str), repeat = times)]
	
	
def search(pattern, text):
	shift = computeShifts(pattern)
	startPos = 0
	matchLen = 0
	ans = 0
	for c in text:
		while matchLen >= 0 and pattern[matchLen] != c:
			startPos += shift[matchLen]
			matchLen -= shift[matchLen]
		matchLen += 1
		if matchLen == len(pattern):
			#yield startPos
			ans += 1
			startPos += shift[matchLen]
			matchLen -= shift[matchLen]
	return ans
# Construct shift table used in KMP matching
#
# Time analysis: each iteration of either loop increases shift+pos
# This quantity starts at 0 and ends at most at 2*p
# So total time is O(p).
#
def computeShifts(pattern):
	shifts = [None] * (len(pattern) + 1)
	shift = 1
	for pos in range(len(pattern) + 1):
		while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
			shift += shifts[pos-shift-1]
		shifts[pos] = shift
	return shifts

	
def solve(K, L, S):
	possible = getAll(K, S)
	possible = map(joinTuple, possible)
#	return possible
#	print possible
	expected = 0.0
	worst = -1
	for each in possible:
		num = search(L, each)
		expected += num
		if num >= worst:
			worst = num
#	print worst, expected	
	return worst - expected/len(possible)	


#f = open("A-small-attempt0.in", 'r')
f = open("B-small-attempt0.in", 'r')
f2 = open("outputBananaSmall.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	
	l = f.readline().strip().split()
	S = int(l[2])
	K = f.readline().strip()
	L = f.readline().strip()
	print K, L, S
	if i == t-1:
		f2.write(s+str(solve(K, L, S)))
	else:
		f2.write(s+str(solve(K,L,S))+'\n')

f.close()
f2.close()
