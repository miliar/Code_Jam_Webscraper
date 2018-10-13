INPUT = "pancakes.txt"
OUTPUT = "pancakes.out"

def check(pancakes):
	for p in pancakes:
		if p == '-':
			return False
	return True


def flip(pancakes, start, K):
	for i in range(start, start + K):
		if pancakes[i] == '+':
			pancakes[i] = '-'
		else:
			pancakes[i] = '+'


def solve(pancakes, K):
	answer = 0
	N = len(pancakes)
	for i in range(N - K + 1):
		if pancakes[i] == "-":
			flip(pancakes, i, K)
			answer += 1

	if check(pancakes):
		return answer
	return "IMPOSSIBLE"


def main(input_path, output_path):
	input_file = open(input_path, 'r')
	output_file = open(output_path, 'w')
	T = input_file.readline()
	T = int(T)
	for t in range(1, T + 1):
		pancakes, K = input_file.readline().split()
		pancakes = list(pancakes)
		K = int(K)
		answer = solve(pancakes, K)
		output_file.write("Case #{}: {}\n".format(str(t), str(answer)))


main(INPUT, OUTPUT)