
f = open('inLarge.txt', 'r')

num_cases = int(f.readline())

case_num = 0
for line in f.readlines():
	case_num += 1

	ch = line.strip().split(' ')
	
	num_buttons = ch.pop(0)

	o_loc = 1
	b_loc = 1
	next_o_loc = 1
	next_b_loc = 1

	stack = []
	o_stack = [1]
	o_dif = [1]
	b_stack = [1]
	b_dif = [1]

	for i in range(0, len(ch), 2):
		v = int(ch[i+1])
		if ch[i] == 'O':
			o_stack.append(v)
			o_dif.append(abs(v - o_stack[len(o_dif)-1]))
		elif ch[i] == 'B':
			b_stack.append(v)
			b_dif.append(abs(v - b_stack[len(b_dif)-1]))
		stack.append(ch[i])

	next_o_loc = o_stack.pop()
	next_b_loc = b_stack.pop()

	#print o_dif
	#print b_dif

	val = 0
	while len(stack) > 0:
		hall = stack.pop(0)
		#print hall
		if hall == 'O' and len(o_dif) > 1:
			mv = o_dif.pop(1)
	
			if mv >= 0:
				if len(b_dif) > 1:
					b_dif[1] -= mv + 1
				val += mv + 1
				#print mv+1
			else:
				if len(b_dif) > 1:
					b_dif[1] -= 1
				val += 1
				#print 1
		elif hall == 'B' and len(b_dif) > 1:
			mv = b_dif.pop(1)

			if mv >= 0:
				if len(o_dif) > 1:
					o_dif[1] -= mv + 1
				val += mv + 1
				#print mv+1
			else:
				if len(o_dif) > 1:
					o_dif[1] -= 1
				val += 1
				#print 1

		#print o_dif
		#print b_dif

	print 'Case #%d: %d' % (case_num, val) 
