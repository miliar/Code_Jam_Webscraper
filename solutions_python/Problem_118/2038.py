import sys
import math

sys.stdin = open("C-large-1.in")
num_cases = int(raw_input())
upper_limit = 1e14

def isPalindrome(a):
	a = str(a)
	return a == a[::-1]

def searchPalindromeInRange(upper_limit):
	begin_sqrt = 1
	end_sqrt = int(math.ceil(math.sqrt(upper_limit)))
	square_list = [ i*i for i in range(begin_sqrt, end_sqrt) if isPalindrome(i) ]
	result = [ i for i in square_list if isPalindrome(i) == True]
	return result

result = searchPalindromeInRange(upper_limit)

for i in range(0, num_cases):
	begin, end = [int(j) for j in raw_input().split()]
	case_result = [k for k in result if k>=begin and k<=end]
	print "Case #%s: %s" %(i+1, len(case_result))
