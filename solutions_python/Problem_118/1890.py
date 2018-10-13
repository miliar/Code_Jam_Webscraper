from math import *

def file_read(file):
	file_open = open(file, 'r')
	
	for line in file_open:
		yield line
	
	file_open.close()
	
def is_palindrome(arg):
	arg = str(arg)
	
	for i in xrange(len(arg)/2):
		if arg[i] != arg[len(arg) -1 -i]:
			return False
	
	return True

def isqr(num):
	old_x = num/2
	while True:
		if old_x == 0:
			new_x = 0
			break;
		new_x = 0.5*(old_x + num/old_x)
		if abs(new_x - old_x) < 0.5:
			break
		old_x = new_x
	return long(floor(new_x))

def get_count(A,B):
	rt1 = isqr(A)
	sq1 = rt1 ** 2
	if sq1 == A:
		rt1 -= 1
		sq1 = rt1 ** 2
		
	rt2 = rt1 + 1
	sq2 = rt2 ** 2
	diff = sq2 - sq1
	
	count = 0
	while sq2 <= B:
		if is_palindrome(sq2):
			rt2 = isqr(sq2)
			if is_palindrome(rt2):
				count += 1
		
		diff += 2
		sq2 += diff
	
	return count

input = file_read('C-small-attempt0.in')
output = open("C-small-attempt0.out","w")

T = int(input.next())

for k in xrange(T):
	arr = input.next().split()
	output.write("Case #"+str(k+1)+": "+str(get_count(long(arr[0]), long(arr[1])))+"\n")
