from __future__ import print_function
t = int(input())
for i in range(1, t+1):
	f = 0
	first = 0
	lane=[]
	out=[]
	n, m = [int(x) for x in raw_input().split(" ")]
	out=[[0 for hhh in range(m)] for jjj in range(n)]
	for j in range(n):
		store = raw_input()
		if f == 0 and store.count('?')!=m:
			f = 1
			first = j
		lane.append(store)
	for k in range(first, n):
		prev = -1
		for l in range(m):
			if lane[k][l] != '?':
				for g in range(prev + 1, l + 1):
					out[k][g] = lane[k][l]
				prev = l
		if prev != -1:
			for last in range(prev, m):
				out[k][last] = out[k][prev]
		else:
			out[k] = out[k-1]
	for top in range(first):
		out[top] = out[first]
	print('Case #{}:'.format(i))
	for a in range(n):
		for b in range(m):
			print(out[a][b], end='')
		print()