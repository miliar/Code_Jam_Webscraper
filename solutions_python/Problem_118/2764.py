import sys
import math

def is_palindrome(num):
	s = str(num)
	if len(s) == 1:
		return True
	#end if
	isOddLen = len(s)%2 == 1
	i = 0
	j = len(s)-1
	isPal = True
	while i < j and s[i] == s[j]:
		i = i + 1
		j = j - 1
	#end while
	return i >= j
	
def num_fair_and_square(a,b):
	c = 0
	for i in range(a,b+1):
		n = math.sqrt(i)
		if n == math.floor(n) and is_palindrome(i) and is_palindrome(int(n)):
			c = c + 1
		#end if
	#end for
	return c
	
def main(args):
	f = open(args[1])
	lines = f.readlines()
	f.close()
	
	if len(lines) == 0:
		exit(0)
	#end if
	
	t = int(lines[0])
	for i in range(t):
		input = lines[i+1].split(" ")
		print "Case #{0}: {1}".format(i+1, num_fair_and_square(int(input[0]),int(input[1])))
	#end for

if __name__ == "__main__":

	main(sys.argv)
	#print is_palindrome(int(sys.argv[1]))
	#print num_fair_and_square(int(sys.argv[1]),int(sys.argv[1]));
#end if