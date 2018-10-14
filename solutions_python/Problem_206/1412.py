
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	end, horses = raw_input().split(" ")
	end = int(end)
	horses = int(horses)
	longest = 0.0
	for j in range(1, horses+1):
		shj, vhj = raw_input().split(" ")
		shj = int(shj)
		vhj = float(vhj)
		if end - shj > 0:
			thj = (end - shj) / vhj
			longest = max(longest, thj)

	print "Case #{}: {}".format(i, end/longest)