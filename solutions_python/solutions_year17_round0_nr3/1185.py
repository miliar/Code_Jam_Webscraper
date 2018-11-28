cases = int(raw_input())


def insert_sorted(lst, num):
	for i in xrange(len(lst)):
		if lst[i][1] == num:
			lst[i][0] += 1
			break
		elif lst[i][1] < num:
			lst.insert(i, [1, num])
			break
	else:
		lst.append([1, num])

for i in xrange(cases):
	input_line = raw_input().split(" ")
	stalls, people = [[1, int(input_line[0])]], int(input_line[1])

	for j in xrange(people - 1):
		if stalls[0][0] == 1:
			stall = stalls.pop(0)[1]
		else:
			stall = stalls[0][1]
			stalls[0][0] -= 1

		insert_sorted(stalls, stall / 2)
		if stall % 2 == 0:
			insert_sorted(stalls, stall / 2 - 1)
		else:
			insert_sorted(stalls, stall / 2)

	stall = stalls.pop(0)[1]
	s_max = stall / 2
	s_min = stall / 2
	if stall % 2 == 0:
		s_min -= 1

	print "Case #{0}: {1} {2}".format(i+1, s_max, s_min)
