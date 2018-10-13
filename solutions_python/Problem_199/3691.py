def flip(c):
	if (c == '+'):
		return '-'
	else:
		return '+'

cases = int(input())

for case in range(cases):
	rawstring = input()
	chars = list(rawstring.split()[0])
	size = int(rawstring.split()[1])
	numFlips = 0
	for index in range(len(chars)-size+1):
		if (chars[index] == '-'):
			numFlips += 1
			for charIndex in range(index, index+size):
				chars[charIndex] = flip(chars[charIndex])
	foundMinus = False
	for c in chars[len(chars)-size+1 : ]:
		if (c == '-'):
			foundMinus = True
			break
	if (foundMinus):
		print ("Case #", case+1, ": ", 'IMPOSSIBLE', sep='')
	else:
		print ("Case #", case+1, ": ", numFlips, sep='')
