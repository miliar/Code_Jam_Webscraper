
def nextTidy(num_list):
	l = len(num_list)
	if l <= 1:
		return num_list

	num_list = [num_list[0]] + nextTidy(num_list[1:])
	if int(num_list[0]) > int(num_list[1]):
		if num_list[0] == '0':
			num_list = '0'*len(num_list)
		else:
			num_list[0] = str( int(num_list[0]) - 1 )
			num_list[1:] = '9'*(len(num_list)-1)

	return num_list

def outputTidy(num_str):
	output = nextTidy(list(num_str))
	if output[0] == '0':
		output = output[1:]
	return ''.join(output)

f_out = open('B-large.out', 'w')
with open('B-large.in') as f_in:
	T = int(f_in.readline())
	for i in xrange(T):
		num = str(f_in.readline().strip('\n'))
		f_out.write('Case #' + str(i+1) + ': ')
		f_out.write(outputTidy(num) + '\n')
