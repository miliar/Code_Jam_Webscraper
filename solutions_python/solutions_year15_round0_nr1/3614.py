def ovation(smax, s):
	add, standing = 0,0
	if smax == 0 or s == None:
		return 0

	standing += int(s[0])

	for i in range(1, len(s)):
		si = int(s[i])
		ti = i
		if si > 0  and ti > standing:
			add += ti - standing
			standing += add
		standing += si

	return add


import json
def main():
	f = open('ovation.in')
	o = open('ovation.out', 'w')
	lines = f.readlines()
	cases = int(lines[0])
	for x in range(0, cases):
		line = lines[x+1].replace("\n", "").split(" ")
		smax = int(line[0])
		s = line[1]
		o.write("Case #%s: %s\n" % (x+1, ovation(smax, s)))

if __name__ == "__main__":
	main()