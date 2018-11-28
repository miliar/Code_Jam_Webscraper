def solve(N, unis):
	R = unis[0]
	Y = unis[2]
	B = unis[4]
	max_num = max(R,Y,B)
	min_num = min(R,Y,B)
	ans = ""
	if R == max_num:
		max_c = "R"
		min_c = "Y" if Y == min_num else "B"
		rem_c = "B" if Y == min_num else "Y"
	elif Y == max_num:
		max_c = "Y"
		min_c = "R" if R == min_num else "B"
		rem_c = "B" if R == min_num else "R"
	else:
		max_c = "B"
		min_c = "Y" if Y == min_num else "R"
		rem_c = "R" if Y == min_num else "Y"

	if max_num != N - max_num:
		while max_num != N - max_num and min_num > 0:
			ans += (max_c + rem_c + min_c)
			max_num -= 1
			min_num -= 1
			N -= 3
		if max_num != N - max_num:
			return "IMPOSSIBLE"
	#if (Y-R == B - R and Y - R > 0):
	#	for i in range(Y-R):
	#		ans +="YB"
	#	for i in range(R):
	#		ans +="YBR"
	#	return ans
	#elif(R - Y == B - Y and R - Y > 0):
	#	for i in range(Y-R):
	#		ans +="RB"
	#	for i in range(R):
	#		ans +="RBY"
	#	return ans
	#elif(R - B == Y - B and R - B > 0):
	#	for i in range(Y-R):
	#		ans +="RY"
	#	for i in range(R):
	#		ans +="RYB"
	#	return ans
	#else:
	for i in range(min_num):
		ans+= (max_c + min_c)
	for i in range(N - max_num - min_num):
		ans+= (max_c + rem_c)
	return ans


if __name__=='__main__':
	turns = int(raw_input())
	for turn in range(turns):
		ins = [int(c) for c in raw_input().split(" ")]
		N = ins[0]
		unis = ins[1:]
		ans = solve(N, unis)
		print "Case #" + str(turn+1) + ": " + ans
