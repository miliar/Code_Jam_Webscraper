def make_set(line):
	return set([int (a) for a in line.strip().split(' ')])


input_file = open('input.txt','r')
lines = input_file.readlines()

num_out = int(lines[0])


for i in xrange(num_out):
	l_1 = set([int (a) for a in lines[i*10 + int(lines[i*10 + 1]) + 1].strip().split(' ')])
	l_2 = set([int (a) for a in lines[i*10 + 6 + int(lines[i*10 + 6])].strip().split(' ')])
	result = l_1.intersection(l_2)
	if len(result) == 1:
		print 'Case #'+str(i+1)+': '+ str(next(iter(result)))
	elif len(result) == 0:
		print 'Case #'+str(i+1)+': Volunteer cheated!'
	else:
		print 'Case #'+str(i+1)+': Bad magician!'
	

