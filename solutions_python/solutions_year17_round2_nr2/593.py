t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	raw_types = str(raw_input()).split()
	n = int(raw_types[0])
	result = 'POSSIBLE'
	last_added = False

	types = {'R':0, 'O':0, 'Y':0, 'G':0, 'B':0, 'V':0}
	colors = {'R':0, 'Y':0, 'B':0}
	mixes = {'O':0,'G':0,'V':0}
	
	types['R'] = int(raw_types[1])
	colors['R'] += int(raw_types[1])
	
	types['O'] = int(raw_types[2])
	colors['R'] += int(raw_types[2])
	colors['Y'] += int(raw_types[2])

	types['Y'] = int(raw_types[3])
	colors['Y'] += int(raw_types[3])

	types['G'] = int(raw_types[4])
	colors['B'] += int(raw_types[4])
	colors['Y'] += int(raw_types[4])

	types['B'] = int(raw_types[5])
	colors['B'] += int(raw_types[5])

	types['V'] = int(raw_types[6])
	colors['R'] += int(raw_types[6])
	colors['B'] += int(raw_types[6])

	mixes['O'] = types['O']
	mixes['G'] = types['G']
	mixes['V'] = types['V']

	circle = []

	if max(colors.values()) > 0.5 * n:
		result = 'IMPOSSIBLE'

	elif types['O'] > types['B']:
		result = 'IMPOSSIBLE'		

	elif types['G'] > types['R']:
		result = 'IMPOSSIBLE'

	elif types['V'] > types['Y']:
		result = 'IMPOSSIBLE'

	else:	
		for mix in mixes.keys():
			if mix == 'O':
				if types['O'] > 0:
					for k in range(types['O']):
						circle.append('B')
						circle.append('O')
						types['B'] -= 1
						types['O'] -= 1
						colors['B'] -= 1
						colors['R'] -= 1
						colors['Y'] -= 1
						mixes['O'] -= 1
					if sum(types.values()) > 0 and types['B'] > 0:
						circle.append('B')
						types['B'] -= 1
						colors['B'] -= 1
						last_added = 'B'
					elif sum(types.values()) > 0 and types['B'] == 0:
						result = 'IMPOSSIBLE'

			elif mix == 'G':
				if types['G'] > 0:
					for k in range(types['G']):
						circle.append('R')
						circle.append('G')
						types['R'] -= 1
						types['G'] -= 1
						colors['B'] -= 1
						colors['R'] -= 1
						colors['Y'] -= 1
						mixes['G'] -= 1
						last_added = 'G'
					if sum(types.values()) > 0 and types['R'] > 0:
						circle.append('R')
						types['R'] -= 1
						colors['R'] -= 1
						last_added = 'R'
					elif sum(types.values()) > 0 and types['R'] == 0:
						result = 'IMPOSSIBLE'

			elif mix == 'V':
				if types['V'] > 0:
					for k in range(types['V']):
						circle.append('Y')
						circle.append('V')
						types['Y'] -= 1
						types['V'] -= 1
						colors['B'] -= 1
						colors['R'] -= 1
						colors['Y'] -= 1
						mixes['V'] -= 1
						last_added = 'V'	
					if sum(types.values()) > 0 and types['Y'] > 0:
						circle.append('Y')
						types['Y'] -= 1
						colors['Y'] -= 1
						last_added = 'Y'
					elif sum(types.values()) > 0 and types['Y'] == 0:
						result = 'IMPOSSIBLE'
			
		# after placing mixes, now place single colors smartly
		while sum(types.values()) > 0:
			if last_added == False:
				max_type = max(types, key=types.get)
				circle.append(max_type)
				types[max_type] -= 1
				colors[max_type] -= 1
				last_added = max_type
			else:
				if last_added == 'B':
					if types['R'] > types['Y']:
						circle.append('R')
						types['R'] -= 1
						colors['R'] -= 1
						last_added = 'R'
					else:
						circle.append('Y')
						types['Y'] -= 1
						colors['Y'] -= 1
						last_added = 'Y'

				elif last_added == 'R':
					if types['B'] > types['Y']:
						circle.append('B')
						types['B'] -= 1
						colors['B'] -= 1
						last_added = 'B'
					else:
						circle.append('Y')
						types['Y'] -= 1
						colors['Y'] -= 1
						last_added = 'Y'

				elif last_added == 'Y':
					if types['R'] > types['B']:
						circle.append('R')
						types['R'] -= 1
						colors['R'] -= 1
						last_added = 'R'
					else:
						circle.append('B')
						types['B'] -= 1
						colors['B'] -= 1
						last_added = 'B'

		if circle[0] == circle[-1]:
			circle = circle[:-2] + [circle[-1]] + [circle[-2]]
			if circle[0] == circle[-1]:
				result = 'IMPOSSIBLE'

	if result == 'POSSIBLE':
		print  "Case #{0}: {1}".format(i, "".join(circle))
	else:
		print  "Case #{0}: {1}".format(i, result)