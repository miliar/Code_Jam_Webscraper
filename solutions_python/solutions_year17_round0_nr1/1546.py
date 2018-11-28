

def main():
	num_tests = int(input())
	for case in range(num_tests):
		solve_pancake_row(case+1)

def solve_pancake_row(case):
	input_line = input().split(' ')
	pancakes = [1 if x == '+' else -1 for x in input_line[0]]
	flipper_size = int(input_line[1])

	flip_count = 0
	for i in range(len(pancakes) - flipper_size + 1):
		if pancakes[i] == -1:
			flip(pancakes, i, flipper_size)
			flip_count += 1


	if any(x == -1 for x in pancakes):
		flip_count = 'IMPOSSIBLE'

	print("Case #{}: {}".format(case, flip_count))

def flip(pancakes, pos, flip_size):
	for k in range(flip_size):
		pancakes[pos+k] *= -1

main()

