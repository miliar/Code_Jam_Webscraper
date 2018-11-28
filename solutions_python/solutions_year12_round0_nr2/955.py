input = open('B-large.in')
output = open('B-large.out', 'w')
num_of_lines = int(input.readline())
num = 0
while num < num_of_lines:
	tokens = input.readline().split()
	N = int(tokens[0])
	S = int(tokens[1])
	p = int(tokens[2])
	t = tokens[3:]
	
	max_num = 0
	sup_possibility = 0
	for ti in t:
		ti = int(ti)
		if ti >= (p * 3) - 2:
			max_num += 1
		elif ti >= (p * 3) - 4 and ti > 0:
			sup_possibility += 1
	max_num += min(S, sup_possibility)
	
	output.write('Case #' + str(num + 1) + ': ' + str(max_num) + '\n')
	num += 1
output.close()
