def flip(pancakes, left_index, spatula_size):
	for i in range(left_index, left_index + spatula_size):
		pancakes[i] = not pancakes[i]

def solve(pancakes, spatula_size):
	"""Flip left-to-right."""
	flips = 0
	for left_index in range(0, len(pancakes) - spatula_size + 1):
		if not pancakes[left_index]:
			flips += 1
			flip(pancakes, left_index, spatula_size)
			# print('FLIP: ', pancakes)

	return flips if all(pancakes) else 'IMPOSSIBLE'

def main():
	cases = int(input())
	for case_num in range(1, cases + 1):
		pancakes, spatula_size = input().split()
		solution = solve([p == '+' for p in pancakes], int(spatula_size))
		print('Case #{}: {}'.format(case_num, solution))

if __name__ == '__main__':
	main()