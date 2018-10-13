def get_line():
	return [str(i) for i in raw_input().strip().split()]

for T in range(int(raw_input())):
	S_max, people = get_line()
	count = 0
	index = 0
	shyness = []
	people_standing = 0
	for c in people:
		if people_standing >= index:
			people_standing += int(c)
		else:
			while count + people_standing < index:
				count += 1
			people_standing += int(c)
		index += 1
	with open("A-large.out", "a") as f:
		f.write("Case #{0}: {1}\n".format(T+1, count))
