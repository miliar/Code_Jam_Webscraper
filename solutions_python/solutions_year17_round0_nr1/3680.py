import sys

def do_flip_k(pancakes, start, K):
	for i in range(K):
		if pancakes[start + i] == '+':
			pancakes[start + i] = '-'
		else:
			pancakes[start + i] = '+' 

def do_flip(pancakes, K):
	sol = 0

	if len(pancakes) < K:
		return -1

	for i in range(len(pancakes) - K):
		if pancakes[i] == '-':
			sol += 1
			do_flip_k(pancakes, i, K)
	
	check = pancakes[len(pancakes) - K]

	for i in range(len(pancakes) - K + 1, len(pancakes)):
		if pancakes[i] != check:
			return -1

	return sol if check == '+' else sol + 1




def flip(file_name):
	test_count = 0
	with open(file_name,'r') as infile:
		test_count = int(infile.readline())
		for i in range(test_count):
			test_line = infile.readline()
			sol = do_flip(list(test_line.split()[0]), int(test_line.split()[1]))
			print("case #" + str(i + 1) + ": " + (str(sol) if sol >=0 else "IMPOSSIBLE"))


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage: ProblemA file_name")
	flip(sys.argv[1])