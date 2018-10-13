import sys

rounds = int(sys.stdin.readline())

count = 1

for line in sys.stdin:
	if count == rounds+1 :
		break
	o_pos = 1
	b_pos = 1

	tokens = line.split()

	buttons = int(tokens[0])
	i = 1

	o_list = []
	b_list = []
	act = []
	
	for i in range(1,len(tokens), 2):
		if tokens[i]=='O':
			o_list.append(int(tokens[i+1]))
			act.append('O')
		else:
			b_list.append(int(tokens[i+1]))
			act.append('B')

	i = 0
	j = 0
	time = 0

	while i<len(o_list) and j<len(b_list):
		o_diff = o_list[i] - o_pos
		b_diff = b_list[j] - b_pos
		if act[i+j] == 'O':
			o_pos = o_list[i]
			i += 1
			time += abs(o_diff) + 1
			b_mov = min(abs(o_diff)+1, abs(b_diff))
			if b_diff < 0:
				b_pos -= b_mov
			else:
				b_pos += b_mov
		else:
			b_pos = b_list[j]
			j += 1
			time += abs(b_diff) + 1
			o_mov = min(abs(b_diff)+1, abs(o_diff))
			if o_diff < 0:
				o_pos -= o_mov
			else:
				o_pos += o_mov

	while i<len(o_list):
		o_diff = o_list[i] - o_pos
		o_pos = o_list[i]
		i += 1
		time += abs(o_diff) + 1

	while j<len(b_list):
		b_diff = b_list[j] - b_pos
		b_pos = b_list[j]
		j += 1
		time += abs(b_diff) + 1

	print("Case #" + str(count) + ": " + str(time))
	count += 1
print
