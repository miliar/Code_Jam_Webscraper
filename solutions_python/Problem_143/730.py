inp = open('input.dat','r')
out = open('output.dat','w')

for case in xrange(int(inp.readline())):
	if case != 0:
		out.write('\n')
	inp_numbers = input_info = [int(x) for x in inp.readline().split(' ')]

	A = input_info[0]
	B = input_info[1]
	K = input_info[2]

	counter = 0

	for old_machine in xrange(A):
		for new_machine in xrange(B):
			if old_machine & new_machine < K:
				counter+=1

		output = "Case #{}: {}".format(case+1,counter)

	out.write(output)

inp.close()
out.close()
