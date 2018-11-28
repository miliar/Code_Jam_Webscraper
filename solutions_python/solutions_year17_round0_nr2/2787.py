#! /usr/local/Cellar/python3/3.6.1/bin/python3

nb_tests = int(input())

for t in range(nb_tests):
	n = list(input())

	for i in range(len(n) - 1, 0, -1):
		if i == 0:
			break

		if n[i] >= n[i - 1]:
			continue

		n[i - 1] = chr(ord(n[i - 1]) - 1)

		for j in range(i, len(n)):
			n[j] = "9"

	tidy = "".join(n).lstrip("0")

	print("Case #" + str(t + 1) + ": " + tidy)
