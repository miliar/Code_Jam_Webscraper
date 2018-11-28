import sys


def do (C, F, X, n):

	t = 0

	for i in range(n):
		t = t + C / (2 + F * i)


	#print C, F, X, n, t + X / (2 + F * n)
	return t + X / (2 + F * n)

f = open(sys.argv[1])
T = int(f.readline().strip())

for t in range(T):
	(C, F, X) = f.readline().strip().split()
	C = float(C)
	F = float(F)
	X = float(X)

	#ans = X / 2
	#for i in range(int(X)):
	#	ans = min(ans, do(C, F, X, i))
		#print i, ans
	#print "Case #" + str(t + 1) + ":", ans

	#i = 0
	#ans = do (C, F, X, 0)
	#while True:
	#	i = i + 1
	#	nans = do(C, F, X, i)
	#	if (nans > ans):
	#		break
	#	else:
	#		ans = nans

	#print "Case #" + str(t + 1) + ":", ans

	l = 0
	vl = do(C, F, X, l)
	step = 2

	while True:
		r = l + step
		vr = do(C, F, X, r)
		c = (r + l) / 2
		vc = do(C, F, X, c)

		#print l, c, r
		#print vl, vc, vr
		if vc < vl and vc < vr:
			break
		elif vl < vc and vl < vr:
			break
		else:
			step = step * 2
		
	
	while (c - l) > 1 and (r - c) > 1:
		lc = (l + c) / 2
		cr = (c + r) / 2

		vlc = vl = do(C, F, X, lc)
		vcr = vl = do(C, F, X, cr)

		ind = [l, lc, c, cr, r]
		v = [vl, vlc, vc, vcr, vr]
		#print ind
		#print v
		for i in [1, 2, 3]:
			if v[i] < v[i - 1] and v[i] < v[i + 1]:
				break

		l, c, r = ind[i - 1], ind[i], ind[i + 1]
		vl, vc, vr = v[i - 1], v[i], v[i + 1]
		#print l, c, r

	print "Case #" + str(t + 1) + ":", min(vl, vc, vr)

#print C, F, X