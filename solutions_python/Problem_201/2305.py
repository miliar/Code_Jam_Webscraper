testcase_count = int(input())
for testcase_index in range(testcase_count):
	n, k = map(int, input().split())
	stalls = dict()
	stalls[n] = 1
	#print(stalls)
	for i in range(k):
		s = sorted(stalls.keys(), reverse=True)[0]
		stalls_right = s // 2
		stalls_left = s // 2 if s % 2 == 1 else s // 2 - 1
		if stalls[s] == 1:
			del stalls[s]
		else:
			stalls[s] -= 1
		stalls[stalls_right] = stalls[stalls_right] + 1 if stalls_right in stalls.keys() else 1
		stalls[stalls_left] = stalls[stalls_left] + 1 if stalls_left in stalls.keys() else 1
			
		#print(stalls)

	print("Case #%d: %d %d" % (testcase_index + 1, stalls_right, stalls_left))
	
