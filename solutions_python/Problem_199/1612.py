def optimized(pancake_input):
	pancakes = []

	i = 0
	while i < len(pancake_input):
		if pancake_input[i] == '+':
			pancakes.append(1)
		elif pancake_input[i] == '-':
			pancakes.append(0)
		else:
			break
		i += 1

	size = int(pancake_input[i+1:])

	flips = 0
	for i in range(0, len(pancakes)-size+1):
		if pancakes[i] == 0:
			flips += 1
			for j in range(i+1,i+size):
				pancakes[j] = 0 if pancakes[j] == 1 else 1

	for i in range(len(pancakes)-size+1, len(pancakes)):
		if pancakes[i] == 0:
			return "IMPOSSIBLE"

	return str(flips)


if __name__ == "__main__":

	with open("large_output", 'w') as fout:
		f = open("A-large.in")
		n = int(f.next())
		for i in range(n):
			line = f.next().strip()
			fout.write("Case #"+str(i+1)+": "+optimized(line.rstrip())+"\n")
		f.close()
