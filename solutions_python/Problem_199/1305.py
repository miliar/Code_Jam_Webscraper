import codejam

for (number, line) in enumerate(codejam.input("A")):
	(p, k) = line.split(" ")
	k = int(k)
	pancakes = list(map(lambda x: x == "+", list(p)))
	flips = 0
	for i in range(len(pancakes) + 1 - k):
		if not pancakes[i]:
			flips += 1
			for j in range(i, min(i + k, len(pancakes))):
				pancakes[j] = not pancakes[j]
	if all(x for x in pancakes):
		codejam.case(flips)
	else:
		codejam.impossible()

codejam.finish()