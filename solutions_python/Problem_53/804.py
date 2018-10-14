import sys

def main(argv):
	input = open(argv[1], 'r')
	output = open(argv[2], 'w')

	inputCount = int(input.readline())

	masks = []
	for i in range(31):
		j = 1 << i
		masks.append(j-1)

	for i in range(inputCount):
		result = False
		line = input.readline()

		splitline = line.split(' ')
		N = int(splitline[0])
		K = int(splitline[1])

		if K&1:
			if not (K+1)&masks[N]:
				result = True

		if result == True:
			output.write('Case #' + str(i+1) + ': ON\n')
		else:
			output.write('Case #' + str(i+1) + ': OFF\n')

if __name__ == "__main__":
	main(sys.argv)
