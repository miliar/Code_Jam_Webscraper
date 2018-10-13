#! /usr/local/Cellar/python3/3.6.1/bin/python3

nb_tests = int(input())

for t in range(nb_tests):
	pancakesstr, kstr = input().split()
	pancakes = list(pancakesstr)
	k = int(kstr)
	y = 0
	impossible = False

	for i in range(len(pancakes)):
		if pancakes[i] == "+":
			continue

		y += 1

		if i + k > len(pancakes):
			print("Case #" + str(t + 1) + ": IMPOSSIBLE")
			impossible = True
			break

		if i + k - 1 < len(pancakes):
			j = 0
			for j in range(k):
				if pancakes[i + j] == "-":
					pancakes[i + j] = "+"
				else:
					pancakes[i + j] = "-"

	if not impossible:
		print("Case #" + str(t + 1) + ": " + str(y))
