"""

code jam
Qualification Round 2013
Problem C. Fair and Square

"""
import math
import time
start = time.time()

in_file = open('input/csmall.txt', 'r')
out_file = open('output/csmall.txt', 'w')

cache = {}
def is_palindrome(num):
	s = str(num)
	if s == '':
		return True
	else:
		if s[0] == s[-1]:
			return is_palindrome(s[1:-1])
		else:
			return False

def is_fair_square(num):
	snum = str(num)
	if snum in cache:
		return cache['snum']
	if is_palindrome(num):
		rt = math.sqrt(num)
		if int(rt) == rt:
			if is_palindrome(int(rt)):
				cache['snum'] = True
				return True
	cache['snum'] = False

def my_method(lower, upper):
	counter = 0
	for i in range(lower, upper + 1):
		if is_fair_square(i):
			#print i
			counter += 1
	return counter

testcases = int(in_file.readline())

j = 1
while j <= testcases:
	nextline = in_file.readline().split()
	n1 = int(nextline[0])
	n2 = int(nextline[1])
	result = my_method(n1, n2)
	outline = "Case #" + str(j) + ": " + str(result)
	print >> out_file, outline
	j += 1

"""print my_method(100, 1000)
print is_fair_square(121)	"""

#print is_palindrome('aab')
in_file.close()
out_file.close()

print "Elapsed time is " +  str(time.time() - start)