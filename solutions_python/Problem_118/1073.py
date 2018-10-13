import sys
import math
from itertools import *

def isPalindrome(i):
	s = str(i)
	L = len(s)
	for x in range(L):
		if s[x] != s[L - 1 - x]:
			return False
	return True

# bigPow = 14
# bigPowHalf = 8
# bigPowQuarter = 4

bigPow = 100
bigPowHalf = 50
bigPowQuarter = 25

pow_ten_bigpow = pow(10, bigPow)

all_fairsquare = [1,4,9]

# generate all the integer fair&square palins that exist:
for string in combinations_with_replacement('012', bigPowQuarter):
	for middle in ['0', '1', '2', '']:
		string = str(int(''.join(string)))

		# generate the palindrome that starts with string
		# (we know it's be a palindrome because we construct
		# it that way)
		palin = string + middle + string[::-1]

		# check if square is a palindrome
		squared = int(palin) * int(palin)

		if squared <= pow_ten_bigpow and isPalindrome(squared) and squared != 0:
			all_fairsquare.append(squared)

all_fairsquare.sort()

# read through the cases and generate output
T = int(sys.stdin.readline());
for t in range(T):

	# get the range we want
	AB = sys.stdin.readline().strip().split(' ')
	A = int(AB[0])
	B = int(AB[1])

	# count the palindromes in this range
	count = 0

	for palindrome in all_fairsquare:
		if palindrome >= A and palindrome <= B:
			count += 1
	print('Case #' + str(t+1) + ': ' + str(count))