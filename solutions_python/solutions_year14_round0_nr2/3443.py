
def main():
	infile = open('P2.in')
	outfile = open('P2.out', 'w')
	n = int(infile.readline())
	for j in range (0,n):
		line = infile.readline().split()
		result = solve(float(line[0]),float(line[1]),float(line[2]))
		res = "Case #%d: %f \n" % (j+1, result)
		outfile.write(res)
	infile.close()
	outfile.close()

def solve(c,f,x):
	nofarm = x/2
	print nofarm
	prev = nofarm
	fnum = 1
	faster = True

	while faster:
		current = gen(c,f,x,fnum)
		if current > prev:
			faster = False
		else:
			fnum = fnum + 1
			prev = current

	return prev

def gen(c,f,x,fnum):
	total = 0
	for i in range(0,fnum):
		total = total + (c/((i*f)+2))
	total = total + x/((fnum*f) + 2)
	return total
main()