
for x in range(int(raw_input())):
	num_list = raw_input().split(' ')
	s_max = num_list[0]
	num_list = map(int,num_list[1])
	num_standing = 0
	num_to_add = 0
	for index,num in enumerate(num_list):
		if num == 0:
			pass
		if index <= num_standing:
			num_standing += num
		else:
			while num_standing < index:
				num_standing += 1
				num_to_add += 1
			num_standing += num
	print 'Case #%d: %d' % (x + 1, num_to_add)


