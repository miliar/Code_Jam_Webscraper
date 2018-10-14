T = int(raw_input())
for t in range(1, T+1):
	line = map(int, raw_input().split())
	N, S, p = line[0:3]
	nums = line[3:]
	answer = 0
	surp = 0
	for num in nums:
		if num == 0:
			if p == 0:
				answer += 1
		elif num % 3 == 0:
			if int(num / 3) >= p:
				answer += 1
			elif int(num / 3) + 1 >= p:
				surp += 1
		elif num % 3 == 1:
			if int(num / 3) + 1 >= p:
				answer += 1
		elif num % 3 == 2:
			if int(num / 3) + 1 >= p:
				answer += 1
			elif int(num / 3) + 2 >= p:
				surp += 1
	print "Case #{0}: {1}".format(t, answer + min(surp, S))
