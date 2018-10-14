f_in = open('A-large.in')
f_out = open('output_large', 'w')
data_in = f_in.readlines()
case = int(data_in[0])
def solve(string):
	accumulate = 0
	addition = 0
	for i in range(0, len(string)):
		if (0 == i):
			if (string[0] == '0'):
				addition += 1
				accumulate = 1

			else:
				accumulate = (int(string[0]))
		else:
			if (i <= accumulate):
				accumulate += int(string[i])
			else:
				addition += 1
				accumulate += (int(string[i])+1)
	return addition


for i in range(1, case+1):
	string = data_in[i].split(' ')[1].strip()
	f_out.write('Case #' + str(i) + ': ' + str(solve(string)) + '\n')



