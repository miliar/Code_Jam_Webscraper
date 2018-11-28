import math

def count(a, b):
	counter = 0
	lBound = int(math.ceil(a ** 0.5))
	uBound = int(math.floor(b ** 0.5))
	for i in range(lBound, uBound + 1):
		init = str(i)
		pal = str(i * i)
		if init == init[::-1]:
			if pal == pal[::-1]:
				counter += 1

	return counter

inp = open('C-small-attempt1.in', 'r')
out = open('C-small1.out', 'w')


tests = int(inp.readline()[:-1])

for i in range(tests):
	parse = inp.readline()[:-1]
	dup = parse.split()
	a, b = int(dup[0]), int(dup[1])
	# print a, b
	writing = 'Case #' + str(i + 1) + ': ' + str(count(a, b)) + '\n'
	out.write(writing)

# print count(100, 1000)
