tests = int(raw_input())
for case in range(tests):
	arr = raw_input().split()
	line = list(arr[0])
	window_size = int(arr[1])
	i = 0
	length_line = len(line)
	last_index = window_size - 1
	possible = True
	k = 0
	while last_index < length_line:
		while line[i] == '+' and last_index < length_line:
			i += 1
			last_index += 1
		if last_index < length_line:
			for j in range(i,last_index+1):
				if line[j] == '+':
					
					line[j] = '-'
				else:
					line[j] = '+'
			k += 1
	for j in range(i,length_line):
		if line[j] == '-':
			possible = False
	if possible:
		print "Case #" + str(case + 1) + ":",k
	else:
		print "Case #" + str(case + 1) + ":","IMPOSSIBLE"
			