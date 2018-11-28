t = int(raw_input())

rows = []
flip_sizes = []
for i in range(0, t):
	in_str = raw_input()
	flip_sizes.append(int(in_str.split(' ')[1]))
	row_str = in_str.split(' ')[0]
	row = []
	for bit in row_str:
		if bit == '+':
			row.append(True)
		else:
			row.append(False)
	rows.append(row)

flip_counts = []

for i in range(0, t):
	flip_counts.append(0)
	for pos in range(0, len(rows[i]) - flip_sizes[i] + 1):
		if rows[i][pos] == False:
			for sub_pos in range(0, flip_sizes[i]):
				rows[i][pos+sub_pos] = not rows[i][pos+sub_pos]
			flip_counts[i] += 1

for i in range(0, t):
	solved = True
	for bit in rows[i]:
		if bit == False:
			solved = False
			break

	out_str = "Case #" + str(i+1) + ": "
	if solved:
		out_str += str(flip_counts[i])
	else:
		out_str += "IMPOSSIBLE"

	print out_str