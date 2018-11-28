#!/usr/bin/env python3

# N + 2 stalls per row (left and right occupied)
# K people
# Return min(left space, right space), max(left space, right space) of last person

input = open('C-small-1-attempt1.in')
out = open('C-small-1-output.txt', 'w')
lines = input.readlines()
num_cases = lines[0]
cases = lines[1:]

for case_num, case in enumerate(cases):
	if case_num >= num_cases:
		print 'I HAVE MORE CASES THAN EXPECTED'

	[n, k] = case.split(' ')
	n = int(n)
	k = int(k)
	#print('n: ' + str(n) + ' k:' + str(k))

	# build up n stalls
	stalls = [0] * (n+2)
	stalls[0] = 1
	stalls[-1] = 1

	#For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

	# process k people
	for i in range(k):
		#print 'i: ' + str(i)
		computed_stalls = [None] * (n+2)
		for j in range(n+2):
			if stalls[j] == 1:
				computed_stalls[j] = (0, 0)
			else:
				l = 0
				for z in range(j-1, 0, -1):
					if stalls[z] == 0:
						l += 1
					else:
						break
				r = 0
				for z in range(j+1, n+1, 1):
					if stalls[z] == 0:
						r += 1
					else:
						break
				computed_stalls[j] = (l, r)

		#print(computed_stalls)

		max_min_s = 0
		max_min_j = 0
		for j in range(n+2):
			local_min = min(computed_stalls[j])
			if local_min > max_min_s:
				max_min_s = local_min
				max_min_j = j
		#print 'max_min_s: ' + str(max_min_s) + ' max_min_j: ' + str(max_min_j)

		max_max_s = 0
                max_max_j = 0
		for j in range(n+2):
			local_min = min(computed_stalls[j])
			local_max = max(computed_stalls[j])
			if local_min == max_min_s and local_max > max_max_s:
				max_max_s = local_max
				max_max_j = j
		#print 'max_max_s: ' + str(max_max_s) + ' max_max_j: ' + str(max_max_j)

		stalls[max_max_j] = 1
		#print stalls

	#for i in range(k):
	#	computed
	#	print(i)

	case_output = 'Case #'+ str(case_num+1) + ': ' + str(max_max_s) + ' ' + str(max_min_s)
	print(case_output)
	out.write(case_output + '\n')

out.close()
