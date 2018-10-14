import math

def is_square(n):
    return sqrt(n).is_integer()

lines = [line.rstrip('\n') for line in open('input.in')]

cases = int(lines[0])

for i in range(1, cases + 1):
	search = [int(x) for x in lines[i].split(" ")]
	count = 0
	for x in range(search[0], search[1] + 1):
		square = int(math.sqrt(x))
		str_square = str(square)
		str_x = str(x)
		if square ** 2 == x and str_square == str_square[::-1] and str_x == str_x[::-1]:
			count += 1
	print("Case #%s: %s" % (i, count))