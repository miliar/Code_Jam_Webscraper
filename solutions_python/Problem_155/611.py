import sys

def calc_ovation(smax, ov):
	if smax == 0:
		return 0

	# find "gaps" that require extra people
	cur_s = 0
	invite = 0
	for i in xrange(smax+1):
		cur_ov = cur_s + invite
		if cur_ov < i:
			invite += i - cur_ov

		cur_s += int(ov[i])

	return invite

if __name__ == '__main__':
	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file("solution.dat", "wb")

	for i in xrange(int(lines[0])):
		(smax, ov) = lines[i+1].split(' ')
		out.write("Case #%d: %d\n" % (i + 1, calc_ovation(int(smax), ov)))

	out.close()