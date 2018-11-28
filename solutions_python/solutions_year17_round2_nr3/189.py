t = int(input())

for t_i in range(t):
	n, q = map(int, input().split())
	horses = [None]*n
	for n_i in range(n):
		ei, si = map(int, input().split())
		horses[n_i] = (ei, si)
	
	distances = [-1]*n
	for n_i in range(n-1):
		distances[n_i] = list(map(int, input().split()))[n_i+1]
	input()
	uk, vk = map(int, input().split()) #useless
	
	current = [(horses[0][0], horses[0][1], 0)]
	for i in range(n-1):
		dist = distances[i]
		next = []
		for cheval in current:
			if cheval[0]-dist >= 0:
				next.append((cheval[0]-dist, cheval[1], cheval[2]+dist/cheval[1]))
		min_t = min(next, key=lambda x:x[2])[2]
		next.append((horses[i+1][0], horses[i+1][1], min_t))
		current = next
	min_t = min(current, key=lambda x:x[2])[2]
	print("Case #%d: %.7f" % (t_i+1, min_t))