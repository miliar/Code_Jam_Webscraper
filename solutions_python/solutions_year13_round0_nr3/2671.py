import math
def show(lst):
	for i in lst:
		print i

def process(a,b):
	counter = 0
	for i in range(a,b+1):
		if fair_and_square(i):
			# print i
			counter += 1
	return str(counter)

	
def palindrome(n):
	return str(n) == ''.join(list(reversed(str(n))))

def fair_and_square(n):
	tf, root = square(n)
	if tf:
		if palindrome(n) and palindrome(root):
			return True
	return False

def square(n):
	root = int(math.sqrt(n))
	return root**2 == n, root


lines = [line.strip() for line in open('input.txt')]

n = int(lines[0]);

for i in range(n):
	[a,b] = map(int,lines[i+1].split())
	print "Case #" + str(i+1) + ": " + process(a,b)




# 0 1 4 9 16 25 36 49
# 1 3 5 7 9  11 13 15 