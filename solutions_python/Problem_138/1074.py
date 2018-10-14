input = open('D-large.in', 'r')
output = open('output.txt', 'w')

test_case_count = int(input.readline())
#process test case one by one
for i in range(test_case_count):
	#store relevant data
	N = float(input.readline())
	naomi = sorted(str.strip(input.readline()).split(' '))
	ken = sorted(str.strip(input.readline()).split(' '))

	#initialize variables for deceitful war
	pair_count = 0
	stop_condition = False

	n_idx = 0
	k_idx = 0

	#deceitful war
	while (not stop_condition):
		if naomi[n_idx] > ken[k_idx]:
			pair_count += 1
			n_idx += 1
			k_idx += 1
		else:
			n_idx += 1
		if n_idx == N:
			stop_condition = True

	#initialize variables for war
	ken_win_count = 0
	stop_condition = False

	n_idx = 0
	k_idx = 0

	#war
	while (not stop_condition):
		if naomi[n_idx] > ken[k_idx]:
			k_idx += 1
		else:
			ken_win_count += 1
			n_idx += 1
			k_idx += 1
		if k_idx == N:
			stop_condition = True

	y = pair_count
	z = N - ken_win_count
	#print output
	output.write("Case #%d: %d %d\n" %(i+1, y, z))