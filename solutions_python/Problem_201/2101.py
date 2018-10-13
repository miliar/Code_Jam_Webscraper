def find_min_max(pos, start, end):
	return (end - start - 1) // 2,  (end - start) // 2

def find_stall(stalls, start, end):

	if end - start == 0:
		return start, 0, 0

	best_pos = (start + end - 1) // 2
	best_stall = stalls[best_pos]
	if best_stall == False:
		min_s, max_s = find_min_max(stalls, start, end)
		return best_pos, min_s, max_s

	else:
		left_pos, left_min, left_max = find_stall(stalls, start, best_pos)
		right_pos, right_min, right_max = find_stall(stalls, best_pos + 1, end)
		if left_min > right_min:
			return left_pos, left_min, left_max
		elif right_min > left_min:
			return right_pos, right_min, right_max
		elif left_max >= right_max:
			return left_pos, left_min, left_max
		else:
			return right_pos, right_min, right_max


num_tests = int(input())
results = ['' for i in range(num_tests)]

for i in range(num_tests):

	num_stalls, num_peop = [int(x) for x in input().split()]

	stalls = [False for j in range(num_stalls)]

	for j in range(num_peop):
		pos, min_s, max_s = find_stall(stalls, 0, num_stalls)
		stalls[pos] = True

	results[i] = 'Case #{}: {} {}'.format(i + 1, max_s, min_s)

for i in range(num_tests):
	print(results[i])
