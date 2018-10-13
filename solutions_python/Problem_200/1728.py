tests = int(raw_input())
for case in range(tests):
	num = list(raw_input())
	length = len(num)
	
	if length == 1:
		print "Case #" + str(case+1) + ": " + "".join(num)
		continue
	
	position = 0
	while position < len(num) - 1 and num[position] <= num[position + 1]:
		position += 1
	if position == length - 1:
		print "Case #" + str(case+1) + ": " + "".join(num)
	elif num[position] == num[0] and num[position] == '1':
		print "Case #" + str(case+1) + ": " + "".join(['9' for i in range(length - 1)])
	elif num[position] == num[0]:
		digit = chr(ord(num[0]) - 1)
		length1 = 1
		length2 = len(num) - 1
		print "Case #" + str(case+1) + ": " + "".join([digit for i in range(length1)]) + "".join(['9' for j in range(length2)])
	else:
		substr = num[0:position]
		ans = []
		ans.extend(substr)
		ans.append(chr(ord(num[position]) - 1))
		length = len(num[position+1:])
		ans.extend(['9' for i in range(length)])
		print "Case #" + str(case+1) + ": " + "".join(ans)