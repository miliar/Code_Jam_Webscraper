def find_unhapines(case, R, C, N):
	data = [[0 for _ in range(C) ]for _ in range(R)]
	case_d = case
	c = 0

	g = R*C / R

	#print bin(case)
	#print data
	#print case
	while case > 0:
		b = 1 & case
		case >>= 1
		if b:
			u,p =  c/g , c%g
			#print case, R, C, N
			#print u,p
			data[u][p] = 1

		c  += 1

	ans = 0
	for j in range(C-1):
		for i in range(R):
			if data[i][j] + data[i][j+1] == 2:
				ans += 1

	for j in range(C):
		for i in range(R-1):
			if data[i][j] + data[i+1][j] == 2:
				ans += 1

	#if ans == 7:
	#	print case_d
	#	print bin(case_d)
	#	print data
	#print data
	return ans

#print find_unhapines(255, 2, 3, 0)

def solution(R, C, N):
	#print "--"
	#print R,C,N
	unhappiness = 999999999999

	for i in range((1 << R*C) ):
		if bin(i).count('1') == N:
			x = find_unhapines(i, R, C, N)
			if x < unhappiness:
				unhappiness = x

	return unhappiness


T = int(raw_input())

for test in range(1, T+1):

	r, c, n = map(int, raw_input().split())

	answer = 0

	print "Case #{}: {}".format(test, solution(r,c,n))
