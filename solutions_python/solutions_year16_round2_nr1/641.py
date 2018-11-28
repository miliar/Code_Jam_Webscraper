def getNumber(text):
	letters = list(text)
	number = list()

	while "Z" in letters:
		number.append("0")
		for x in "ZERO":
			letters.remove(x)

	while "W" in letters:
		number.append("2")
		for x in "TWO":
			letters.remove(x)

	while "U" in letters:
		number.append("4")
		for x in "FOUR":
			letters.remove(x)

	while "X" in letters:
		number.append("6")
		for x in "SIX":
			letters.remove(x)

	while "G" in letters:
		number.append("8")
		for x in "EIGHT":
			letters.remove(x)

	while "O" in letters:
		number.append("1")
		for x in "ONE":
			letters.remove(x)

	while "H" in letters:
		number.append("3")
		for x in "THREE":
			letters.remove(x)

	while "F" in letters:
		number.append("5")
		for x in "FIVE":
			letters.remove(x)

	while "V" in letters:
		number.append("7")
		for x in "SEVEN":
			letters.remove(x)

	while "I" in letters:
		number.append("9")
		for x in "NINE":
			letters.remove(x)

	string = ""
	for y in sorted(number):
		string+=y

	return string


testcases = int(input())
for i in range(1, testcases+1):
	print("Case #%d: %s" % (i, getNumber(input())))