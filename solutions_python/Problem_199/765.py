n= int(input().strip())
for i in range(0, n):
	line = input().strip().split()
	row = line[0]
	new_row = []
	count = 0
	for c in row:
		new_row.append(c)
	flipper = int(line[1])
	j = 0
	while j < len(new_row) - flipper + 1:
		if new_row[j] == "-":
			for k in range(j, j + flipper):
				if new_row[k] == "-":
					new_row[k] = "+"
				else:
					new_row[k] = "-"
			count += 1
		j += 1
	if "".join(new_row[len(new_row)-flipper:]) == "+"*flipper:
		a = count
	else:
		a = "IMPOSSIBLE"
	print("Case #{}: {}".format(i+1, a))