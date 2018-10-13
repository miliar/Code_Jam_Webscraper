def main():
	lines = open('B-large.in').readlines()
	cases = int(lines[0])
	for x in xrange(cases):
		line = [float(y) for y in lines[x+1].split()]
		c = line[0]
		f = line[1]
		xn = line[2]

		rate = 2.0
		current = 0.0
		fintime = (xn - current) / rate
		factime = (c - current) / rate
		pt = fintime+1
		while (pt > fintime):
			pt = fintime
			rate += f
			fintime = (xn - current) / rate + factime
			factime += (c - current) / rate
		print "Case #{0}: {1:.7f}".format(x+1, pt)

if __name__=='__main__':
	main()	
