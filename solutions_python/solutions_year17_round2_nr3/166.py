def p3(N,horses,distances):
	path = [[0,horses[0][0],horses[0][1]]]
	for i in range(N-1):
		#Going from i to i+1
		dist = distances[i][i+1]
		path_n = []
		for p in path:
			if p[1] < dist:
				#Too tired horse
				continue
			#else
			time = dist/p[2]
			path_n.append([time+p[0], p[1] - dist, p[2]])
			
		mini = min([p[0] for p in path_n])
		path_n.append([mini, horses[i+1][0], horses[i+1][1]])

		path = path_n

	return min([p[0] for p in path])
	
	
	
	
T = int(input())
for t in range(T):
	N,Q = list(map(int,input().split()))
	horses = []
	for i in range(N):
		horses.append(list(map(float,input().split())))

	distances = []
	for i in range(N):
		distances.append(list(map(float,input().split())))
		
	investigate = []
	for i in range(Q):
		investigate.append(list(map(int,input().split())))
	
	print("Case #%d: %s"%(t+1,p3(N,horses,distances)))
