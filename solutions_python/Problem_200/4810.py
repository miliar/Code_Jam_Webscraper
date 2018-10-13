def parse(filed):
	flag = 0
	vals = []
	f = open(filed)
	for line in f:
		if (flag == 1):
			i = int(line)
			res = isOk(i)
			vals.append(res)
		else:
			flag = 1
	return vals

def isOk(number):
	while (number > 0):
		tmp = number;
		while tmp > 9:
			j = tmp % 10
			if j < ((tmp / 10) % 10):
				tmp = -5
			elif tmp > 9:
				tmp /= 10
		if tmp >= 0:
			return number
		number -= 1

def formater(vals):
	f = open('output.txt', 'w')
	for i, val in enumerate(vals):
		s = 'Case #' + str(i + 1) + ': ' + str(val) + '\n'
		f.write(s)

formater(parse("input.in"))
