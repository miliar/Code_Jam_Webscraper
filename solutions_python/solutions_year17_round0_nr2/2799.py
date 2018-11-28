import sys


def parseCase(fin):
	return next(fin).strip()


def solve(digits):
	digits = list(map(int, digits))
	top = 0
	for i in range(len(digits)-1):
		first = digits[i]
		second = digits[i+1]
		if first <= second:
			top = i+1
		else:
			break

	#nothing to fix
	if top == len(digits)-1:
		return "".join(map(str, digits))

	start = digits.index(digits[top])
	digits[start] -= 1
	for i in range(start+1, len(digits)):
		digits[i] = 9

	if digits[0] == 0:
		digits = digits[1:]
	return "".join(map(str, digits))


def main(filenameIn, filenameOut):
	with open(filenameIn, 'rt') as fin, open(filenameOut, 'wt') as fout:
		line = next(fin).strip()
		count = int(line)
		for i in range(count):
			digits = parseCase(fin)
			answer = solve(digits)
			fout.write("Case #{}: {}\n".format(i+1, answer))

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
