fs = []
for x in xrange(1, 10):
	y = str(x*x)
	if y == y[::-1]: fs.append(int(y))
for i in xrange(0, 4):
	for j in xrange(10**i, 10**(i+1)):
		x = int(str(j) + str(j)[::-1])
		y = str(x*x)
		if y == y[::-1]: fs.append(int(y))
	for j in xrange(10**i, 10**(i+1)):
		for k in xrange(10):
			x = int(str(j) + str(k) + str(j)[::-1])
			y = str(x*x)
			if y == y[::-1]: fs.append(int(y))
T = int(raw_input())
for tt in xrange(T):
	(A, B) = map(int, raw_input().split(" "))
	r = 0
	for x in fs:
		if A <= x <= B: r += 1
	print("Case #"+str(tt+1)+": "+str(r))
