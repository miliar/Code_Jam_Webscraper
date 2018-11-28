def time_given_number_of_farms(n):
	return (X + n*C + memo[n] * F) / (2 + n * F)

for case in range(1,int(raw_input())+1):
	C, F, X = map(float,raw_input().split())
	
	memo = [0] * (int(X/C)+1)
	memo[0] = 0
	for i in range(1,len(memo)):
		memo[i] = memo[i-1] + C / (2 + (i-1) * F)
	for i in range(1,len(memo)):
		memo[i] += memo[i-1]
	
	ans = min(time_given_number_of_farms(n) for n in range(int(X/C)+1))
	print('Case #%d: %s'%(case,ans))
