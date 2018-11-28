n = int(input().strip())
for i in range(0, n):
	number = input().strip()
	'''
	a = False
	while not a:
		tmp_number = str(number)
		prev = int(tmp_number[0])
		b = True
		for d in tmp_number:
			if int(d) < prev:
				b = False
			prev = int(d)
		if b:
			a = True
		number -= 1
	print("Case #{}: {}".format(i+1, number + 1))
	'''
	n = []
	for l in number:
		n.append(l)
	number = n
	if number[0] == "1" and number.count("0") > 0 and number.count("1") + number.count("0") == len(number):
		new = "9"* (len(number)-1)
	else:
		number = list(map(int, number))
		b = True
		while b:
			a = True
			j = 0
			while j < len(number) - 1:
				if number[j] > number[j+1]:
					number[j] -= 1
					new = number[:j+1] + [9] * (len(number)-j-1)
					j = len(number)
					a = False
				j += 1
			if a:
				new = number
				b = False
			number = new
	number = list(map(str, new))
	number = "".join(number)
	number = int(number)
	print("Case #{}: {}".format(i+1, number))
