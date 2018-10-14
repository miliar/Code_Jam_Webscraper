# python 2.7
import sys

# Not used
def generateFairAndSquare(n, dig=1, sumSq=0):
	if (2*dig==n):
		return [11*i for i in xrange(4) if sumSq+2*i*i < 10]
	elif (2*dig-1==n):
		return [i for i in xrange(4) if sumSq+i*i < 10]

	L = []
	for i in xrange(4):
		if (dig == 1 and i == 0):
			continue
		L += [i*10**(n+1-2*dig) + l*10 + i for l in generateFairAndSquare(n, dig+1, sumSq+2*i*i)]
	return L

def isPalindrome(n):
	s = str(n)

	for i in xrange((len(s)+1)//2):
		if s[i] != s[-i-1]:
			return False
	return True

# Every digit must be less than 4, or there would be a digit that is at least 4^2, which would overflow
# The first digit cannot overflow, since there would be no way to get the same 1st and last digit
# Ex: If we had a first digit of 9, we would have 81 as 1st two digits and 1 at the last. However, to
#get a 1st digit of one, the previous would have to overflow by 19, even though the maximum is near 16
# Therefore, following this reasoning, no number can overflow
# This function generates the fair and square numbers of len n, by adding a digit to those of len n-2 
#(or a digit and d-1 zeroes to those of len n-2d)
def generateFairAndSquareFromPrev(n, Lprev):
	L = []
	for i in xrange(1,4):
		pref = i*10**(n-1)
		for d in xrange(1,1+n/2):
			pot = 10**d
			L += [pref + l*pot + i for l in Lprev[n-2*d] if isPalindrome((pref + l*pot + i)**2)]
	return L

maxN = 51
L = [0]*(maxN+1)
L[0] = [0]
L[1] = [i for i in xrange(4)]
L[2] = [11*i for i in xrange(1,3)]

for i in xrange(3,maxN+1):
	L[i] = generateFairAndSquareFromPrev(i, L)
	#print i, len(L[i])

G = sorted(reduce(lambda x,y:x+y, L, []))

if (len(sys.argv) > 2):
	I = open(sys.argv[-2]).readlines()
	nC = int(I[0])

	fwrite = open(sys.argv[-1], 'w')
	def printTxt(x):
		fwrite.write(x+"\n")
else:
	nC = int(raw_input())
	I = [nC] + [raw_input() for i in xrange(nC)]
	def printTxt(x):
		print(x)

for iC in xrange(1,nC+1):
	a,b = map(int, I[iC].split(" "))
	c = 0
	for i in G:
		if (i**2 < a):
			continue
		if i**2 > b:
			break;
		c += 1
	printTxt("Case #%d: %d"%(iC, c))
