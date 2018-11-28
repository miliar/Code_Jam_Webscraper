import math
case = int(raw_input())
for cn in range(1, case+1):
	N, K = [int(s) for s in raw_input().split(" ")]
	p_array = []
	for line in range(N):
		r, height = [int(s) for s in raw_input().split(" ")]
		p_array.append((r, height))
	
	p_array.sort(reverse=True)
	
	diff_area_seen = {}
	height_area_seen = {}
	flat_area_seen = {}
	
	def flat_area(i):
		if i in flat_area_seen:
			return flat_area_seen[i]
		else:
			ar = p_array[i][0]*p_array[i][0]*math.pi
			flat_area_seen[i] = ar
			return ar
			
	def height_area(i):
		if i in height_area_seen:
			return height_area_seen[i]
		else:
			ar = 2*math.pi*p_array[i][0]*p_array[i][1]
			height_area_seen[i] = ar
			return ar
		
	def diff_area(i, j):
		if (i, j) in diff_area_seen:
			return diff_area_seen[(i, j)]
		else:
			ar = (p_array[i][0]*p_array[i][0]-p_array[j][0]*p_array[j][0])*math.pi
			diff_area_seen[(i, j)] = ar
			return ar
		
	def DFS(comb, tmp, level, start):
		if level == K:
			comb.append(tmp)
			return
		while start < N:
			tmp.append(start)
			DFS(comb, list(tmp), level+1, start+1)
			tmp.pop(-1)
			start += 1
	
	comb = []
	DFS(comb, [], 0, 0)
	max_area = float('-inf')
	
	for inds in comb:
		area = 0
		for i in range(len(inds)-1):
			area += diff_area(inds[i], inds[i+1])
		area += flat_area(inds[-1])
		
		for i in range(len(inds)):
			area += height_area(inds[i])
		max_area = max(max_area, area)
	
	print "Case #"+str(cn)+": "+ str(max_area)

		