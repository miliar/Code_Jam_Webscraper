from math import sqrt
a = [1, 2, 3,
	11, 22, 
	101, 111, 202, 212, 
	1001, 1111, 2002, 
	10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102,
	100001, 101101, 110011, 111111, 200002, 
	1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]
	
f = open('C-small-attempt1.in')
t = int(f.readline())
for ti in xrange(t):
	x, y = [int(val) for val in f.readline().split()]
	i = 0
	while a[i] < sqrt(x):
		i += 1
	j = 0
	while a[j] <= sqrt(y):
		j += 1
	#print x, y, i, j, a[i], a[j]
	print "Case #" + str(ti + 1) + ": " + str(j - i)