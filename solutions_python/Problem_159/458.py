import sys

filename = sys.argv[1]
f = open(filename, 'r')
T = int(f.readline())
for t in range(T):
	N = int(f.readline())
	M = map(lambda x : int(x), f.readline().strip().split(' '))
	
	method1 = 0
	method2 = 0

	method2tot = 0

	prev = -1
	for m in M:
		if prev == -1:
			prev = m
			continue
		if m < prev:
			method1 = method1 + prev - m
			if method2 < (prev - m):
				method2 = prev - m

		prev = m

	for i in range(len(M)-1):
		m = M[i]
		if m > method2:
			method2tot = method2tot + method2
		else:
			method2tot = method2tot + m

	print "Case #" + str(t+1) + ": " + str(method1) + " " + str(method2tot)


