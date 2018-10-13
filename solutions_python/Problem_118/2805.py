# 3.py
import sys
from math import sqrt

# def is_square(apositiveint):
# 	if apositiveint==1:
# 		return True
# 	x = apositiveint // 2
# 	seen = set([x])
# 	while x * x != apositiveint:
# 		x = (x + (apositiveint // x)) // 2
# 		if x in seen:
# 			return False
# 		seen.add(x)
# 	return True
# 	

def is_square(number):
	return sqrt(number) == int(sqrt(number))

def testPalin(n):
	return str(n)[::-1]==str(n)


if len(sys.argv) < 2:
    sys.exit('Usage: %s input-name' % sys.argv[0])

finName = sys.argv[1]

fin = open(finName, 'r')
fout = open("3.out", 'w')

numCase = int(fin.readline())

for index in xrange(numCase):
	count = 0
	lower, upper = [int (i) for i in fin.readline().split(' ')]
	print "lower=", lower, " upper=", upper
	for i in xrange(lower,upper+1):
		if is_square(i) and testPalin(i):
			if(testPalin(int(sqrt(i)))):
				count+=1
	fout.write("Case #%d: %d\n" % ((index+1), count))
