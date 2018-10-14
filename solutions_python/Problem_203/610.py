def cut(cake):
	fill_initial = '?'
	last_uncut_row = -1
	for i in range(len(cake)):
		vertical_cut(cake[i])
		if cake[i][0] == '?': # row is all ?'s?
			if i == 0 or cake[i-1][0] == '?':
				last_uncut_row = i
			else:
				cake[i] = cake[i-1] # copy the previous row
	
	# cut the top of the cake if needed
	if last_uncut_row != -1:
		for i in range(last_uncut_row, -1, -1):
			cake[i] = cake[last_uncut_row + 1] #copy the first cut row

def vertical_cut(row):
	prefill_index = -1
	prefill_initial = '?'
	last_initial = '?'
	for i in range(len(row)):
		if row[i] != '?':
			if prefill_initial == '?': # first character in row
				prefill_index = i
				prefill_initial = row[i]
			last_initial = row[i]
		elif last_initial != '?':
			row[i] = last_initial
	
	if prefill_index != -1:
		row[:prefill_index] = prefill_initial*prefill_index
		
def print_cake(cake):
	for i in range(len(cake)):
		print(''.join(cake[i]))

t = int(input())
for i in range(1, t + 1):
	r_str, c_str = input().split(" ")
	cake = []
	for j in range(int(r_str)):
		row_str = input()
		row = []
		for k in range(int(c_str)):
			row.append(row_str[k])
		cake.append(row)
		
	cut(cake)
	print("Case #{}:".format(i))
	print_cake(cake)
  
  