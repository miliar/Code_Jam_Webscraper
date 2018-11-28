# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def invert(value):
	if (value ):
		return 0
	return 1


def main():
	file_name = "data_input"
	f = open(file_name, "r")
	for i, line in enumerate(f):
	    # process(line)
		if (i == 0):
			numLines = int(line)
			print(numLines)
		else:
			pancakes, flipper = line.split(" ")
			pancakes = pancakes.replace("+", "0")
			pancakes = pancakes.replace("-", "1")
			pancakes = list(pancakes)
			pancakes = map(int, pancakes)
			# print(pancakes)
			hits = 0
			# print(flipper)
			for j in range(0, len(pancakes)-int(flipper)+1):
				if (pancakes[j] == 1):
					hits += 1
					for k in range(0, int(flipper)):
						pancakes[j+k] = invert(pancakes[j+k])
					# print(pancakes)
			# print(hits)
			if (sum(pancakes)):
				print("Case #{}: IMPOSSIBLE".format(i))
			else:
				print("Case #{}: {}".format(i, hits))

	f.close()

if __name__ == "__main__":
    main()



