import math

fil = open("csmlin2.txt", "r")
T = int(fil.readline())

#n**2 = (n-1)**2 + (n - 1) + n

def is_square(n):
	return math.sqrt(n).is_integer()

def is_fair(x):
	if len(str(x)[:-2]) == 1:
		return True
	elif len(str(x)[:-2]) == 2 and list(str(x)[:-2])[0] == list(str(x)[:-2])[1]:
		return True
	return str(x)[:-2] == str(x)[:-2][::-1]

for k in xrange(T):
	results = []
	line = fil.readline().split()
	A, B = int(line[0]), int(line[1])
	if is_square(A) and is_fair(A) and is_fair(math.sqrt(A)):
		results.append(A)
	while A < B:
		A = math.sqrt(A**2 + 2 * A + 1)
		if is_square(A) and is_fair(A) and is_fair(math.sqrt(A)):
			results.append(A)
	print "Case #%d: %d" % (k+1, len(results))