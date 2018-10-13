import sys

data = sys.stdin.readlines()

num_test = int(data[0])

for i in range(1, 1+num_test):
	numbers = data[i].rsplit()
	#print numbers
	n_googlers = int(numbers[0])
	n_surprises = int(numbers[1])
	p_score = int(numbers[2])
	arr_weights = list()
	for j in range(3,3+n_googlers):
		if(int(numbers[j]) >= p_score):
			arr_weights.append(int(numbers[j]) - 3*p_score)
	#print arr_weights
	confirmed = [y for y in arr_weights if y > -3]
	extra = [y for y in arr_weights if y < -2 and y > -5]
	count = len(confirmed) + min(len(extra), n_surprises)
	print 'Case #%d: %d' % (i, count)