with open("A-small-attempt2.in", "r") as f:
	T = int(f.readline())
	for i in range(0, T):
		rows = []
		for j in range(0, 2):
			row_number = int(f.readline())
			for k in range(0, row_number - 1):
				f.readline()
			row = f.readline()
			rows.append(row.split())
			for k in range(0, 4 - row_number):
				f.readline()
		intersection = list(set(rows[0]) & set(rows[1]))
		if len(intersection) == 0:
			print("Case #" + str(i + 1) + ": Volunteer cheated!")
		elif len(intersection) == 1:
			print("Case #" + str(i + 1) + ": " + str(intersection[0]))
		else:
			print("Case #" + str(i + 1) + ": Bad magician!")
