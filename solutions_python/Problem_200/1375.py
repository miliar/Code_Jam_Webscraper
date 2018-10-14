import codejam

for (number, line) in enumerate(codejam.input("B")):
	n = list(line)
	cut = len(n)
	for i in range(1, len(n)):
		while i > 0 and n[i - 1] > n[i]:
			n[i - 1] = str(int(n[i - 1]) - 1)
			cut = i
			i -= 1
		if cut != len(n):
			break
	codejam.case(("".join(n)[0:cut] + "9" * (len(n) - cut)).lstrip("0"))

codejam.finish()