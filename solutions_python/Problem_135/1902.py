#encoding = utf-8
tt = input()
for t in range(tt):
	r1 = input()
	set1 = set()
	for row in range(4):
		num = raw_input()
		nums = num.split(' ')
		if row == r1 - 1:
			set1 |= set(nums)
	r2 = input()
	set2 = set()
	for row in range(4):
		num = raw_input()
		nums = num.split(' ')
		if row == r2 - 1:
			set2 |= set(nums)
	target_set = set1 & set2
	out =  'Case #' + str(t + 1) + ': '
	size = len(target_set)
	if size == 1:
		out += list(target_set)[0]
	elif size > 1:
		out += 'Bad magician!'
	else:
		out += 'Volunteer cheated!'
	print out