num_testcase = int(raw_input())
for i in range(0,num_testcase):
	line = raw_input()

	params = line.split(' ')
	A = int(params[0])
	B = int(params[1])

	counts = 0

	for num in range(A, B+1):
		num_str = str(num)
		for j in range(0, len(num_str)-1):
			num_str = num_str[1:] + num_str[0]
			new_num = int(num_str)
			if new_num > num and new_num <= B:
				# print num, new_num
				counts+=1

	print 'Case #' + str(i+1) + ': ' + str(counts)