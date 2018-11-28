import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	print (case)
	
	line = in_file.readline().replace('\n', '')
	n_stalls = int(line.split(' ')[0])
	r_red = int(line.split(' ')[1])
	o_orange = int(line.split(' ')[2])
	y_yellow = int(line.split(' ')[3])
	g_green = int(line.split(' ')[4])
	b_blue = int(line.split(' ')[5])
	v_violet = int(line.split(' ')[6])
	
	color_counts = []
	color_counts.append(r_red)
	color_counts.append(o_orange)
	color_counts.append(y_yellow)
	color_counts.append(g_green)
	color_counts.append(b_blue)
	color_counts.append(v_violet)
	
	count_red = r_red + o_orange + v_violet
	count_yellow = y_yellow + o_orange + g_green
	count_blue = b_blue + g_green + v_violet
	
	count_total = count_red + count_yellow + count_blue
	
	hair_counts = []
	hair_counts.append(count_red)
	hair_counts.append(count_yellow)
	hair_counts.append(count_blue)
	
	if (count_red > ((1 * float(count_total)) / 2)):
		out_file.write('IMPOSSIBLE')
	elif (count_yellow > ((1 * float(count_total)) / 2)):
		out_file.write('IMPOSSIBLE')
	elif (count_blue > ((1 * float(count_total)) / 2)):
		out_file.write('IMPOSSIBLE')
	else:
		#print (color_counts)
		#print (hair_counts)
		stall_string = ''
		index = 0
		maximum = max(color_counts)
		if (color_counts.count(maximum) > 1):
			hair_index = hair_counts.index(max(hair_counts))
			color_counts_clone = color_counts[:]
			if (hair_index == 0):
				color_counts_clone[2] = 0
				color_counts_clone[3] = 0
				color_counts_clone[4] = 0
			elif (hair_index == 1):
				color_counts_clone[0] = 0
				color_counts_clone[4] = 0
				color_counts_clone[5] = 0
			elif (hair_index == 2):
				color_counts_clone[0] = 0
				color_counts_clone[1] = 0
				color_counts_clone[2] = 0
			index = color_counts_clone.index(max(color_counts_clone))
		else:
			index = color_counts.index(max(color_counts))
		color_counts[index] -= 1
		n_stalls -= 1
		color = color_from_index(index)
		#if (color == 'R'):
		#	hair_counts[0] -= 1
		#elif (color == 'O'):
		#	hair_counts[0] -= 1
		#	hair_counts[1] -= 1
		#elif (color == 'Y'):
		#	hair_counts[1] -= 1
		#elif (color == 'G'):
		#	hair_counts[1] -= 1
		#	hair_counts[2] -= 1
		#elif (color == 'B'):
		#	hair_counts[2] -= 1
		#elif (color == 'V'):
		#	hair_counts[0] -= 1
		#	hair_counts[2] -= 1
		stall_string += color
		while(n_stalls > 0):
			#print (color_counts)
			#print (hair_counts)
			color_counts_clone = color_counts[:]
			hair_counts_clone = hair_counts[:]
			if (color == 'R'):
				color_counts_clone[0] = 0
				color_counts_clone[1] = 0
				color_counts_clone[5] = 0
				hair_counts_clone[0] = 0
			elif (color == 'O'):
				color_counts_clone[0] = 0
				color_counts_clone[1] = 0
				color_counts_clone[2] = 0
				color_counts_clone[3] = 0
				color_counts_clone[5] = 0
				hair_counts_clone[0] = 0
				hair_counts_clone[1] = 0
			elif (color == 'Y'):
				color_counts_clone[1] = 0
				color_counts_clone[2] = 0
				color_counts_clone[3] = 0
				hair_counts_clone[1] = 0
			elif (color == 'G'):
				color_counts_clone[1] = 0
				color_counts_clone[2] = 0
				color_counts_clone[3] = 0
				color_counts_clone[4] = 0
				color_counts_clone[5] = 0
				hair_counts_clone[1] = 0
				hair_counts_clone[2] = 0
			elif (color == 'B'):
				color_counts_clone[3] = 0
				color_counts_clone[4] = 0
				color_counts_clone[5] = 0
				hair_counts_clone[2] = 0
			elif (color == 'V'):
				color_counts_clone[0] = 0
				color_counts_clone[1] = 0
				color_counts_clone[3] = 0
				color_counts_clone[4] = 0
				color_counts_clone[5] = 0
				hair_counts_clone[2] = 0
				hair_counts_clone[0] = 0
			
			maximum = max(color_counts_clone)
			if (color_counts_clone.count(maximum) > 1):
				hair_index = hair_counts_clone.index(max(hair_counts_clone))
				if (hair_index == 0):
					color_counts_clone[2] = 0
					color_counts_clone[3] = 0
					color_counts_clone[4] = 0
				elif (hair_index == 1):
					color_counts_clone[0] = 0
					color_counts_clone[4] = 0
					color_counts_clone[5] = 0
				elif (hair_index == 2):
					color_counts_clone[0] = 0
					color_counts_clone[1] = 0
					color_counts_clone[2] = 0
				index = color_counts_clone.index(max(color_counts_clone))
			else:
				index = color_counts_clone.index(max(color_counts_clone))
			
			color_counts[index] -= 1
			color = color_from_index(index)
			if (color == 'R'):
				hair_counts[0] -= 1
			elif (color == 'O'):
				hair_counts[0] -= 1
				hair_counts[1] -= 1
			elif (color == 'Y'):
				hair_counts[1] -= 1
			elif (color == 'G'):
				hair_counts[1] -= 1
				hair_counts[2] -= 1
			elif (color == 'B'):
				hair_counts[2] -= 1
			elif (color == 'V'):
				hair_counts[0] -= 1
				hair_counts[2] -= 1
			stall_string += color
			n_stalls -= 1
		out_file.write(str(stall_string))
	
	out_file.write('\n')

def color_from_index(index):
	if (index == 0):
		return 'R'
	elif (index == 1):
		return 'O'
	elif (index == 2):
		return 'Y'
	elif (index == 3):
		return 'G'
	elif (index == 4):
		return 'B'
	elif (index == 5):
		return 'V'
	return '?'
	
if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()