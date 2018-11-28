import fileinput

num = 0;
inputs = [];

for line in fileinput.input():
	if fileinput.isfirstline():
		num = int(line)
	else:
		inputs.append(line.split(" "))

def flip(idx, cakes, k):
	for i in range(idx, idx + k):
		if cakes[i] == "-":
			cakes[i] = "+"
		else:
			cakes[i] = "-"

for idx, case in enumerate(inputs):
	k = int(case[1])
	iters = 0
	pancakes = list(case[0])
	flips = 0

	for i in range(len(pancakes) - k + 1):
		if pancakes[i] == "-":
			flip(i, pancakes, k)
			flips+=1

	if "-" in pancakes:
		print("Case #" + str(idx + 1) + ": " + "IMPOSSIBLE")
	else:
		print("Case #" + str(idx + 1) + ": " + str(flips))

