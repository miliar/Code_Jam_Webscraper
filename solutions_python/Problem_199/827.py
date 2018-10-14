
case_count = int(input())

for case in range(case_count):
	
	pan, size = input().split()
	size = int(size)

	val = 0
	pan = list(pan)

	for i in range(len(pan)-size+1):
		if pan[i] == "-":
			for j in range(i, i+size):
				if pan[j] == "-":
					pan[j] = "+"
				else:
					pan[j] = "-"
			val += 1

	for char in pan[-size:]:
		if char == "-":
			val = "IMPOSSIBLE"
			break

	print("Case #{0}: {1}".format(case+1, val))

