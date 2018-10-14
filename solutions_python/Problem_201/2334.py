infile = open("input_file.txt", 'r')
outfile = open("output_file.txt", 'w')

T = int(infile.readline())
for i in range(T):
	inStr = infile.readline().split()
	k = int(inStr[1])
	n = int(inStr[0])

	a1 = 0
	a2 = 0
	b1 = 0
	b2 = 0
	c1 = n
	c2 = 1
	ans = n
	carry = False

	while k > 0:
		ans = c1
		k -= c2
		if c1 % 2 == 0:
			a1 = int(c1 / 2)
			a2 += c2
			b1 = int(c1 / 2) - 1
			b2 += c2

		elif c1 % 2 == 1:
			if carry is False:
				b1 = int((c1 - 1) / 2)
				b2 += 2 * c2
			if carry is True:
				a1 = int((c1 - 1) / 2)
				a2 += 2 * c2

		if carry is True:
			c1 = n1
			c2 = n2
			carry = False

		else:
			c1 = a1
			c2 = a2
			n1 = b1
			n2 = b2
			a1 = 0
			a2 = 0
			b1 = 0
			b2 = 0
			carry = True

	if ans % 2 == 0:
		y = int(ans / 2)
		z = int(ans / 2 - 1)
	else:
		y = int((ans - 1) / 2)
		z = y

	outfile.write("Case #" + str(i + 1) + ": " + str(y) + " " + str(z) + "\n")

