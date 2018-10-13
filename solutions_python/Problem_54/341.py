def gcd(x,y):
    while x:
        x, y = y % x, x
    return y

testcases = open("warning.in").readlines()
t = 1
for tc in testcases[1:]:
	tc = map(lambda x: int(x), tc.split(" ")[1:])
	if len(tc) == 0:
		break
	tc.sort()
	#print tc

	diff = []
	for i in range(len(tc)-1):
		diff += [tc[i+1] - tc[i]]

	T = diff[0]
	for d in diff[1:]:
		T = gcd(T,d)
	
	#print T
	print "Case #%d: %d" % (t, (-tc[0] % T))

	t += 1
