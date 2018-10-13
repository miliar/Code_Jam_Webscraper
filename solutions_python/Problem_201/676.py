import collections

def compute_spaces(stalls):
	"""Return list of (Ls, Rs), one for each location."""
	left_spaces = []
	right_spaces = []

	last_left_filled_index = -1
	for i in range(len(stalls)):
		left_spaces.append(i - last_left_filled_index - 1)
		if stalls[i]:
			last_left_filled_index = i
	
	last_right_filled_index = len(stalls)
	for i in range(len(stalls) - 1, -1, -1):
		right_spaces.append(last_right_filled_index - i - 1)
		if stalls[i]:
			last_right_filled_index = i
	right_spaces = list(reversed(right_spaces))

	return [(i, left_spaces[i], right_spaces[i]) for i in range(len(stalls)) if not stalls[i]]

def brute_solve(num_stalls, num_people):
	stalls = [True] + [False] * num_stalls + [True]
	ls, rs = -1, -1
	for k in range(num_people):
		# print('----- {} -----'.format(k))
		# print(stalls)
		spaces = compute_spaces(stalls)
		# print(spaces)
		sorted_spaces = max(spaces, key=lambda t: (min(t[1], t[2]), max(t[1], t[2]), -t[0]))
		# print(sorted_spaces)
		index, ls, rs = sorted_spaces
		# print(k+1, ls, rs)
		stalls[index] = True
	return max(ls, rs), min(ls, rs)


def split_space(space, q, count):
	if space <= 1:
		return

	half = space // 2
	split = (half, half - 1) if space % 2 == 0 else (half, half)
	try:
		q[split] += count
	except KeyError:
		q[split] = count

def generate_pairs(n):
	"""Add elements to a queue, accessible via OrderedDict."""
	q = collections.OrderedDict()  # Maps (ls, rs) space to number of times it will appear
	split_space(n, q, 1)

	while q:
		(space1, space2), count = q.popitem(last=False)
		yield space1, space2, count
		split_space(space1, q, count)
		split_space(space2, q, count)

def smart_solve(num_stalls, num_people):
	total = 0
	for space1, space2, count in generate_pairs(num_stalls):
		total += count
		# print(space1, space2, count, total)
		if total >= num_people:
			return space1, space2
	return 0, 0

def main():
	cases = int(input())
	for case_num in range(1, cases + 1):
		stalls, people = input().split()
		max_space, min_space = smart_solve(int(stalls), int(people))
		print('Case #{}: {} {}'.format(case_num, max_space, min_space))


if __name__ == '__main__':
	main()