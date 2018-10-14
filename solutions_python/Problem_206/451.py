T =  int(raw_input())

for t in range(T):
	D, N = map(int, raw_input().split())
	horses = []	
	for i in range(N):
		horses.append(map(int, raw_input().split()))

	max_time = (D-horses[0][0])*1.0/horses[0][1]
	for i in range(1, N):
		time = (D-horses[i][0])*1.0/horses[i][1]
		if time > max_time:
			max_time = time
			temp = horses[i]
	ans =  D*1.0/max_time
		
	print "Case #%d: %f" % (t+1, ans)
