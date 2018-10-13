from math import *

## {{{ http://code.activestate.com/recipes/577821/ (r1)
def lsqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = long(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
## end of http://code.activestate.com/recipes/577821/ }}}

def getCountOfFairNumbers(A, B):
	count = 0
	a, b = lsqrt(A), lsqrt(B)
	for i in xrange(a, b+1):
		if A <= i*i and i*i <=B and str(i) == str(i)[::-1] and str(i*i) == str(i*i)[::-1]:
			count += 1
	return count

fin = open('C-small-attempt0.in', 'r')
fout = open('C-small-attempt0.out', 'w')
T = int(fin.readline())
for t in xrange(T):
	[A, B] = fin.readline().split()
	count = getCountOfFairNumbers(long(A), long(B))
	fout.write("Case #" + str(t + 1) + ": " + str(count) + '\n')
fin.close()
fout.close()

