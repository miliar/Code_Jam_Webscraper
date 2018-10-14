import sys
from math import sqrt
def is_square(integer):
	root = sqrt(integer)
	if root.is_integer():
		return (str(long(root)) == str(long(root))[::-1])
	else:
		return False
my_file = open(sys.argv[1], 'r')

tests = int(my_file.readline())

for i in range(tests):
	tx = ((my_file.readline()).rstrip('\n')).split(" ")
	A=long(tx[0])
	B=long(tx[1])
	results = 0

	for v in range(A,B+1):
		if (str(v) == str(v)[::-1]):
			if is_square(v):
				results +=1

	print "Case #{0}: {1}".format((i+1),results)


