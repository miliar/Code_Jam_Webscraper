T = int(raw_input())
cas = 0
f = open('out.txt', 'w')
while T > 0:
	T -= 1
	n = int(raw_input())
	num = map(int, raw_input().split())
	minn = 9999999999
	for i in xrange(1, 1001):
		res = i
		for j in num:
			if j > i:
				res += (j - 1) // i
		minn = min(res, minn)
	cas += 1
	f.write( "Case #" + str(cas) + ": " + str(minn) + '\n')