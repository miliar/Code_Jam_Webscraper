with open(r'D:\my_stuff\Google Drive\documents\SCHOOL\Programming\Python\codejam1.in', 'r') as f:
	sections = f.read().split()[1:]
def combine(*iterables):
	result = []
	for elem in iterables: 
		if isinstance(elem, list): result.extend(elem)
		else: result.append(elem)
	return result
def nChunks(iterable, n):
	return [iterable[i:i+n] for i in range(0, len(iterable), n)]
sections = nChunks(combine(*[combine(*[i for i in sections])]), 4)
final = []
for index in range(1, len(sections)+1):
	s = sections[index-1]
	sSplit = [list(i) for i in s]
	new_s = combine(*[list(i) for i in sSplit])
	z = dict(zip(range(1, 17), new_s))
	ideal_x, ideal_y = {}, {}
	for i in z.keys():
		ideal_x[i] = 'X' if z[i] in ('X', 'T') else z[i]
		ideal_y[i] = 'O' if z[i] in ('O', 'T') else z[i]
	if (ideal_x[1] == ideal_x[2] == ideal_x[3] == ideal_x[4]) and ideal_x[1] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[5] == ideal_x[6] == ideal_x[7] == ideal_x[8]) and ideal_x[5] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[9] == ideal_x[10] == ideal_x[11] == ideal_x[12]) and ideal_x[9] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[13] == ideal_x[14] == ideal_x[15] == ideal_x[16]) and ideal_x[13] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[1] == ideal_x[5] == ideal_x[9] == ideal_x[13]) and ideal_x[1] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[2] == ideal_x[6] == ideal_x[10] == ideal_x[14]) and ideal_x[2] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[3] == ideal_x[7] == ideal_x[11] == ideal_x[15]) and ideal_x[3] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[4] == ideal_x[8] == ideal_x[12] == ideal_x[16]) and ideal_x[4] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[1] == ideal_x[6] == ideal_x[11] == ideal_x[16]) and ideal_x[1] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_x[4] == ideal_x[7] == ideal_x[10] == ideal_x[13]) and ideal_x[4] == 'X': final.append('Case #{}: {}'.format(index, 'X won'))
	elif (ideal_y[1] == ideal_y[2] == ideal_y[3] == ideal_y[4]) and ideal_y[1] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[5] == ideal_y[6] == ideal_y[7] == ideal_y[8]) and ideal_y[5] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[9] == ideal_y[10] == ideal_y[11] == ideal_y[12]) and ideal_y[9] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[13] == ideal_y[14] == ideal_y[15] == ideal_y[16]) and ideal_y[13] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[1] == ideal_y[5] == ideal_y[9] == ideal_y[13]) and ideal_y[1] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[2] == ideal_y[6] == ideal_y[10] == ideal_y[14]) and ideal_y[2] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[3] == ideal_y[7] == ideal_y[11] == ideal_y[15]) and ideal_y[3] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[4] == ideal_y[8] == ideal_y[12] == ideal_y[16]) and ideal_y[4] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[1] == ideal_y[6] == ideal_y[11] == ideal_y[16]) and ideal_y[1] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	elif (ideal_y[4] == ideal_y[7] == ideal_y[10] == ideal_y[13]) and ideal_y[4] == 'O': final.append('Case #{}: {}'.format(index, 'O won'))
	else:
		winner = 'Draw' if '.' not in z.values() else 'Game has not completed'
		final.append('Case #{}: {}'.format(index, winner))
with open(r'D:\my_stuff\Google Drive\documents\SCHOOL\Programming\Python\codejam1results.txt', 'w') as f:
	for outcome in final:
		f.write(outcome + '\n')