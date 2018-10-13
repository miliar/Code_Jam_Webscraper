def last_tidy_number(n):
	tidy = []
	while n > 0:
		tidy.insert(0, str(n % 10))
		n //= 10

	i = len(tidy) - 1
	while i > 0:
		last = int(tidy[i])
		first = int(tidy[i-1])

		if first > last:
			j = i
			while j < len(tidy):
				if tidy[j] == "9":
					break
				tidy[j] = "9"
				j += 1
			tidy[i-1] = str(first - 1)

		i -= 1
	return int("".join(tidy))

t = int(input())
for i in range(1, t + 1):
	n = input()
	print("Case #{}: {}".format(i, last_tidy_number(n)))