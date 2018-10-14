for case in range(int(input())):
	smax, s = input().split()
	friends = 0
	siacc = 0
	for index, sic in enumerate(s):
		siacc += int(sic)
		friends += max(index - siacc - friends + 1, 0)
	print("Case #{}: {}".format(case+1, friends))