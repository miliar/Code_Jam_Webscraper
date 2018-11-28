import math

T = int(input())

for j in range(T):
	ans = 0
	N, P = map(int, input().split(" "))
	R = list(map(int, input().split(" ")))
	Q = list()
	for i in range(N):
		q = list(map(lambda x: int(x)/R[i], input().split(" ")))
		q = list(map(lambda x: list(range(math.ceil(x/1.1), math.floor(x/0.9)+1)), q))
			# [math.ceil(x/1.1), math.floor(x/0.9)], q))
		Q.append(sorted(q))

	# print('Q: ', Q)

	loop = Q[0]
	for q in Q[0]:
		# print('q: ', q)
		# print('Q: ', Q)
		for i in q:
			# print('i: ', i)
			# Check if all package contain this
			kit = []
			for k in Q:
				# for each type
				for h in k:
					# for each package
					if i in h:
						kit.append(h)
						break
			# print('kit: ',kit)
			if len(kit) == N:
				ans += 1
				for k in range(N):
					if k > 0:
						Q[k].remove(kit[k])
				break


	print("Case #" + str(j+1) + ": " + str(ans))