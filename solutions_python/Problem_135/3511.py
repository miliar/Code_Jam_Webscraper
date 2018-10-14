def solve(line1, line2):
	accum = line1 + line2
	if len(set(accum)) == 7:
		return [x for x in accum if accum.count(x) > 1][0]
	if len(set(accum)) == 8:
		return "Volunteer cheated!"
	return "Bad magician!"

def get_line(lines):
	row_index = int(lines[0])
	return lines[row_index]

def to_numbers(list_str):
	return map(int, list_str.split(" "))

def solve_file(filename):
	with open(filename + ".in") as f:
		lines = f.read().splitlines()
	
	count = int(lines[0])

	with open(filename + ".out", "w") as f:
		for index in xrange(0, count):
			pos = index * 10 + 1
			line1 = get_line(lines[pos:pos+5])
			pos += 5
			line2 = get_line(lines[pos:pos+5])
			result = solve(to_numbers(line1), to_numbers(line2))
			f.write("Case #{0}: {1}\n".format(index+1, result))

solve_file("A-small-attempt0")
