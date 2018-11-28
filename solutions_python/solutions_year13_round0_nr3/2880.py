from math import sqrt
no_cases=int(raw_input())

def get_intervals():
	return tuple(map(int,raw_input().split()))
def is_palindrome(number):
	 return str(number)==str(number)[::-1]
def fair_square(interval):
	start,end=interval[0],interval[1]
	palindromes=filter(is_palindrome,list(xrange(start,end+1)))
	return len(map(lambda square:sqrt(square),filter(lambda number: sqrt(number).is_integer(),palindromes)))
intervals=[get_intervals() for i in xrange(no_cases)]

results=[fair_square(interval) for interval in intervals]

for result,i in zip(results,xrange(no_cases)): print "Case #%d: %d" %(i+1,result)
