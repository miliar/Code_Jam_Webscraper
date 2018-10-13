import sys

sys.stdin = open("B-small-attempt0.in", 'r')
sys.stdout = open("out.out", 'w')

T = input()
def check(num):
	a = str(num)
	for i in xrange(len(a) - 1):
		if a[i]>a[i+1]:
			return False
	return True
for t in xrange(1, T+1):
	num = input()
	while (not check(num)):
		num -= 1
	print "Case #%d: %d"%(t, num)
