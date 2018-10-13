import sys

inputs = []

def parse_file(filePath):
	with open(filePath) as f:
		T = int(f.readline())
		for i in range(T):
			(A, B, K) = tuple([int(x) for x in f.readline().split()])
			inputs.append((A, B, K))

def get_answer(A, B, K):
	count = 0
	for a in range(A):
		for b in range(B):
			if (a & b) < K:
				count += 1
	return count

def main():
	parse_file(sys.argv[1])

	currTest = 1
	for (A, B, K) in inputs:
		print('Case #%d: %s' % (currTest, get_answer(A, B, K)))
		currTest += 1

if __name__ == '__main__':
	main()
