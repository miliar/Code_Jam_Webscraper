def solve(D, N, horses):
	horses = sorted(horses, key=lambda h: h[0])
	ans = 0.0
	while len(horses)>0:
		# find smallest time
		min_dist = 1**100
		min_speed = 1
		min_idx = -1
		for i in range(len(horses)-1):
			h1 = horses[i]
			h2 = horses[i+1]
			if h1[1] < h2[1]:
				continue
			if (h2[0]-h1[0]) * min_speed < min_dist * (h1[1] - h2[1]):
				min_idx = i
				min_dist = h2[0] - h1[0]
				min_speed = h1[1] - h2[1]
		if min_idx == -1:
			delta_t = float(D - horses[-1][0])/float(horses[-1][1])
		else: 
			delta_t = float(min_dist)/float(min_speed)
		new_hor = []
		del horses[min_idx]
		for i in range(len(horses)):
			if horses[i][0] + horses[i][1]*delta_t < D:
				new_hor.append( [horses[i][0] + horses[i][1]*delta_t, horses[i][1]])
		horses = new_hor
		ans += delta_t
	return float(D)/ans

if __name__=='__main__':
	turns = int(raw_input())
	for turn in range(turns):
		D, N = [int(c) for c in raw_input().split(" ")]
		horses = []
		for n in range(N):
			k, s = [int(c) for c in raw_input().split(" ")]
			horses.append([k, s])
		ans = solve(D,N,horses)
		print "Case #%d: %f" %(turn+1, ans)
