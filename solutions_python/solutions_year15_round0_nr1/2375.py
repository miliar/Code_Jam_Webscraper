def solve(i):
	Smax, dummy = raw_input().split()
	Smax = int(Smax)
	Si = map(int, list(dummy))
	standing = 0
	friends = 0
	for shyness, people in enumerate(Si):
		if standing < shyness:
			friends += shyness - standing
			standing += people + shyness - standing
		else:
			standing += people

		# print "standing now: ", standing
	print "Case #%s:"%i, friends
T = int(raw_input())
for i in xrange(T):
	T -= 1
	solve(i+1)
