def check(lawn, N, M):
	for n in range(N):
		for m in range(M):
			tn = True
			tm = True
			for cn in range(N):
				if lawn[cn][m] > lawn[n][m]:
					tn = False
					break
			for cm in range(M):
				if lawn[n][cm] > lawn[n][m]:
					tm = False
					break
			if tn == False and tm == False:
				return "NO"
	return "YES"

T = int(raw_input())
for case in range(1, T + 1):
	s = raw_input()
	a = s.split(' ')
	N = int(a[0])
	M = int(a[1])
	lawn = []
	for n in range(N):
		lawn.append([int(i) for i in str(raw_input()) if i != " "])
	print "Case #{0}: {1}".format(case, check(lawn, N, M))