T = int(input())

for t in range(1, T + 1):
	[S_Max, S] = input().split()	

	standing = 0
	friends = 0

	for k in range(int(S_Max) + 1):
		# if not enough standing invite minimum number of friends

		if (standing < k):
			friends += (k - standing)
			standing = k

		standing += int(S[k])
		
	print("Case #{}: {}".format(t, friends))