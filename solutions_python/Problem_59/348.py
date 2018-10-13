T = int(raw_input().strip())
T_counter = 1
while T_counter <= T:
	input = raw_input().strip().split(' ')
	N = int(input[0])
	M = int(input[1])
	direct = dict()
	while N > 0:
		input = raw_input().strip().split('/')
		input = input[1:]
		directPointer = direct
		for item in input:
			if item not in directPointer:
				directPointer[item] = dict()
			directPointer = directPointer[item]
		N = N -1
	ans = 0
	while M > 0:
		input = raw_input().strip().split('/')
		input = input[1:]
		directPointer = direct
		for item in input:
			if item not in directPointer:
				directPointer[item] = dict()
				ans = ans + 1
			directPointer = directPointer[item]
		M = M - 1
	print "Case #%d: %d" % (T_counter, ans)
	T_counter = T_counter + 1

