cases = int(input())
for num in range(cases):
	case = input().split()
	case[0] = int(case[0])
	case[1] = [int(i) for i in list(case[1])]
	people, friends = 0, 0
	for i in range(case[0]+1):
		people += case[1][i]
		if people >= i+1:
			pass
		elif people < i+1:
			people += 1
			friends += 1
	print("Case #{}: {}".format(num+1,friends))
