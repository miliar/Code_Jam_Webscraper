def absorb(armin, motes, result):
	print 'armin', armin
	print 'motes', motes
	print 'result', result
	add = 0
	remove = 0
	if len(motes) == 0:
			return result
	if armin > motes[0]:
		armin = armin + motes[0]
		motes.pop(0)
		return absorb(armin, motes, result)
	elif len(motes) == 1:
		#remove a mote
		motes.pop(0)
		result = result + 1
		return absorb(armin, motes, result)
	#elif armin + armin - 1 > motes[0]:
		#add armin
		#armin = armin + armin - 1
		#result = result + 1
		#arimn = armin + motes[0]
		#motes.pop(0)
		#return absorb(armin, motes, result)
	else:
		while armin <= motes[0] and add < len(motes):
			armin = armin + armin - 1
			add = add + 1
			print 'add', add
		#print len(motes)
		#print 'result', result
		if add < len(motes):
			remove = len(motes)
			result1 = absorb(armin, motes, add + result)
			print 'remove', remove
			print 'result', result
			print 'result1', result1
			result =  min(result + remove, result1)
			return result
		else:
			result = result + len(motes)
			return result


#f = open('sample.txt', 'r')
f = open ('A-large.in', 'r')
f2 = open('output.txt', 'a')
#f2 = open('output2.txt', 'a')

input_number = 1
first_flg = 1
line_number = 1
for line in f:
	line = line.split()
	if first_flg:
		num_of_input = int(line[0])
		first_flg = 0
	elif line_number == 1:
		armin = int(line[0])    
		num_of_motes = int(line[1])
		line_number = 2
	else:
		motes = []
		for i in line:
			motes.append(int(i))
		line_number = 1

		if armin == 1:
			result = len(motes)
		else:
			print 'input_number', input_number
			motes.sort()
			result = 0
			result = absorb(armin, motes, result)

		print 'final_result', result

		f2.write('Case #' + str(input_number) + ': ' + str(result) + '\n')
		input_number = input_number + 1

f2.close()
f.close()