# C.py
import math
import sys

def isFair(num):
	sqrt = int(math.sqrt(num))
	if sqrt != math.sqrt(num): 
		return False
	if str(num) == str(num)[::-1] and str(sqrt) == str(sqrt)[::-1]:
		return True
	else:
		return False

sys.stdin.readline()
q = 1
for line in sys.stdin:
	l = int(line.split()[0])
	u = int(line.split()[1])
	count = 0
	for n in range(l, u+1):
		if isFair(n):
			count = count + 1
	print "Case #%d: %d" % (q,count)
	q= q+1