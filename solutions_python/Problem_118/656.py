import sys
import math
from bisect import bisect_left, bisect_right
import re

fair=[]
square=[]

def main():
	f = open(sys.argv[1])
	T = int(f.readline().strip("\n"))
#	initialize_array(32) #32 is smallest # s.t. x^2 >1000
	initialize_array(10000000) # first big input
	#print fair
	#print square
	for i in range (0,T):
		print "Case #%d: %d" % (i+1, numPalindromes(f))

def initialize_array(limit):
	#print limit
	i = 1
	while i < limit:
		fair.append(i)
		value = i*i
		if isPalindrome(value):
			square.append(value)
			#print i, value
		i = getNextPalindrome(str(i))
		#print i < limit, i, limit

def increment(value, carry, newP):
	value += carry
	if value == 10:
		newP = newP + "0"
		return (1, newP)
	else:
		newP = newP + str(value)
		return (0, newP)

def getNextPalindrome(prev):
	if len(prev)==1:
		if prev=="9": return 11
		else: return int(prev)+1
	
	search = re.compile(r'[^9]').search
	#contains only 9?
	if not bool(search(prev)):
		middle = "0" * (len(prev)-1)
		return int("1"+middle+"1")

	#increase middle
	middle = len(prev)/2
	newP=""
	carry = 1
	#print "middle key: " + prev[middle]
	for i in range(middle, len(prev)):
		carry, newP = increment(int(prev[i]),carry, newP)
	#print "thing to be mirrored: " + newP, newP[:0:-1] + newP
	if(len(prev)%2==0): #even
		return int(newP[::-1] + newP)	
	return int(newP[:0:-1] + newP)

def isPalindrome(value):
	digits = str(value)
	if digits == digits[::-1]: return True
	return False

def numPalindromes(f):
	A,B = [int(s) for s in f.readline().split(" ")]
	start = find_ge(square, A)
	end = find_le(square, B)
	return end-start+1

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

def find_ge(a, x):
	'Find leftmost item greater than or equal to x'
	i = bisect_left(a, x)
	#print i
	if i != len(a):
	    return i
	#raise ValueError
	return len(a)

if __name__ == "__main__":
	main()

