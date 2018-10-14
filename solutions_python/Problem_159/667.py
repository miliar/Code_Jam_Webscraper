f = open("A-large.in", 'r')
ou = open("out", 'w')
inlist = f.readlines()
L = int(inlist[0])

def sln(N, M):
	res1 = 0
	res2 = 0
	ma = 0
	for i in xrange(1, N):
		if M[i] < M[i-1]:
			ma = max(ma, M[i-1] - M[i])
			res1 += M[i-1] - M[i]
	for i in xrange(N - 1):
		if M[i] <= ma:
			res2 += M[i]
		else:
			res2 += ma
	return str(res1) + " " +str(res2)

row = 1
for i in xrange(L):
	N = int(inlist[row])
	row += 1
	M = [int(ch) for ch in inlist[row].split(" ") if ch != '' and ch != '\n']
	print N, M
	row += 1
	ou.write("Case #" + str(i + 1) + ": " + sln(N, M) + '\n')

f.close()
ou.close()
