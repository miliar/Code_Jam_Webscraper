import sys 
import math
f_in = open(sys.argv[1], 'r')
T  =  int(f_in.readline())
r = open(sys.argv[2], 'w')


def is_palindrome(s):
	reverse =  s[::-1]
	if s == reverse:
		return True
	else:
	 return False

def solve(low,high):
	count = 0
	for i in range(low,high+1): 
		if (is_palindrome(str(i))):
			square_root = math.sqrt(i)
			entero = int(square_root)
			if entero==square_root:
				if (is_palindrome(str(entero))):
					count = count + 1
					#print i
	return count


for i in range(T):
        low, high =  [int(x) for x in (f_in.readline().split())]
        #print i,low,high
        r.write("Case #"+str(i+1)+": " + str(solve(low,high)) + '\n')

