def get_grid(f):
	return [map(int, f.readline().split()) for i in range(4)]

def get_possible(grid, row):
	return set(grid[row-1])


def main(filepath):
	f = open(filepath, 'r')
	out = open('magic_trick_out.txt', 'w')
	num_cases = int(f.readline())
	for i in range(num_cases):
		row1 = int(f.readline())
		possible_nums = get_possible(get_grid(f), row1)
		row2 = int(f.readline())
		possible_nums &= get_possible(get_grid(f), row2)
		if len(possible_nums) == 1:
			out.write('Case #%d: %d\n' % ((i+1), possible_nums.pop()))
		elif len(possible_nums) == 0:
			out.write('Case #%d: Volunteer cheated!\n' % (i+1))
		else:
			out.write('Case #%d: Bad magician!\n' % (i+1))

main('A-small-attempt2.in')