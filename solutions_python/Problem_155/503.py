def standing_ovation(s):
	standingup = 0
	friends = 0
	shynes = 0
	for x in s:
		standingup += int(x)
		if standingup < shynes+1:
			friends += 1
			standingup += 1
		shynes += 1
	return friends


def read_and_write(readfrom,writein):
	inp = open(readfrom,'r')
	outp = open(writein, 'w')
	test = int(inp.readline().split(' ')[0])
	for i in xrange(test):
		line = inp.readline()
		a = map(str,line.split(' ')[1])[:len(line)-3]
		b = standing_ovation(a)
		outp.write("Case #%d: %d\n"%(i+1,b))
	inp.close()
	outp.close()

execute=raw_input("Test, small or large?: ")
read = "A-%s-attempt2.in"%(execute)
write = "A-%s-output.txt"%(execute)

read_and_write(read,write)