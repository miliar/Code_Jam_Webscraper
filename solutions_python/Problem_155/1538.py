from Library import *

def solve(values):
	people_standing = 0
	people_needed = 0
	s = values[1]
	for i in range(int(values[0]) + 1):
		if people_standing < i:
			people_needed += i - people_standing
			people_standing += i - people_standing
		people_standing += int(s[i])
	return people_needed

lines = getLines("A-large.in")
out = []

for i in range(int(lines[0])):
	values = [l for l in lines[i + 1].split()]
	res = solve(values)
	out.append("Case #%d: %d"%(i + 1, res))

writeOutLines("outA.txt", out)