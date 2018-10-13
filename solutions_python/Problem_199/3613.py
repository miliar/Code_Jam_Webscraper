
file = open("A-large.in")
output = open("1_output_l", "w")
file.readline()
case_count = 1

for line in file:
	line = line.replace('\n', '').split(' ')
	k = int(line[1])
	s = list(line[0])
	count = 0
	for i in range(0, len(s)-k+1):
		# print(s)
		if s[i] == '-':
			s[i] = '+'
			for j in range(1, k):
				s[i+j] = '+' if s[i+j] == '-' else '-'
			count += 1
	if '-' in s:
		# print("Case #" + str(case_count)+": IMPOSSIBLE\n")
		output.write("Case #" + str(case_count)+": IMPOSSIBLE\n")
	else:
		# print("Case #" + str(case_count)+": "+str(count)+"\n")
		output.write("Case #" + str(case_count)+": "+str(count)+"\n")
	
	case_count += 1