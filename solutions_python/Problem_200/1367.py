def solve(n):
	digits = [int(s) for s in str(n)]
	length = len(digits)
	cont = True

	while cont:
		for index in range(1, length):
			if digits[length - index] < digits[length - index - 1]:
				digits[length - index - 1] -= 1
				digits[length - index - 1] %= 10

				for i in range(1, index + 1):
					digits[length - i] = 9

				break
		else:
			cont = False

	digitsStr = map(str, digits)
	return int("".join(digitsStr))


t = int(raw_input())

for i in xrange(1, t + 1):
	n = int(raw_input())
  #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
 	print "Case #{}: {}".format(i, solve(n))
 