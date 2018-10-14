rounds = int(raw_input())

for i in range(rounds):
	line = raw_input()
	h, arr = line.split()
	h = int(h)
	total = 0
	extra = 0
	for index, num in enumerate(arr):
		num = int(num)
		if total < index:
			add = index - total
			extra += add
			total += add
		total += num

	print "Case #" + str(i + 1) + ": " + str(extra)
