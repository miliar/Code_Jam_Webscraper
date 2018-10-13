PANCAKE_POSITIONS = {'-':'+', '+':'-'}

def get_test_cases():
	n = int(raw_input())
	for i in range(n):
		pancakes_positions, pan_length = raw_input().split()
		yield pancakes_positions, int(pan_length)


def write_output(i, output):
	print "Case #%s: %s" % (str(i + 1), output)


def change_to_opposite(pancake):
	return PANCAKE_POSITIONS[pancake]


def solve(pancakes_positions, pan_length):
	side_to_look_for = '+'
	positions_to_change = set([])
	n_flips = 0
	for position, pancake in enumerate(pancakes_positions):
		if position in positions_to_change:
			side_to_look_for = change_to_opposite(side_to_look_for)
			positions_to_change.remove(position)
		if pancake != side_to_look_for:
			side_to_look_for = change_to_opposite(side_to_look_for)
			positions_to_change.add(position + pan_length)
			n_flips += 1
	positions_to_change.discard(len(pancakes_positions))
	if positions_to_change:
		return "IMPOSSIBLE"
	return n_flips


def main():
	for i, input_data in enumerate(get_test_cases()):
		write_output(i, solve(*input_data))


if __name__ == '__main__':
	main()