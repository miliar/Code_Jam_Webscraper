import sys,math
sys.path.append('../..')
from codejam import get, result

def fair(i): # Is it a palindrome?
	return str(i) == str(i)[::-1]

def square(i): # Is it the square of a palindrome?
	sqrt=math.sqrt(i)
	return ( sqrt==int(sqrt) # It's the square root...
		and fair(int(sqrt)) ) # of a fair (palindromic) number

cases=get.int()
for iCase in range(cases):
	start, end = get.intList()
	n=0
	for i in range(start, end+1): # Range stops one before the end
		if fair(i) and square(i):
			n=n+1
	result(iCase,n)
