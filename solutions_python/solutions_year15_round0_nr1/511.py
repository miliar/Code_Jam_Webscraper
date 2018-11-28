input_file = open("A-large.in")
out = open("output", "w")
n = int(input_file.readline())

for i in range(n):
	additions = 0
	total = 0
	a, b = input_file.readline().split(" ")
	for j, letter in enumerate(b.strip("\n")):
		ta = max(0, j - total)
		additions += ta
		total += ta + int(letter)

	out.write("Case #%d: %d\n" % (i + 1, additions))