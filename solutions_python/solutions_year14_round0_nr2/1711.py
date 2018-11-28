


fi = open("b-in.txt")

for problem in range(int(fi.readline())):

	results = [999999999999]

	c, sf, x = map(float, fi.readline().split(" "))
	fc = 0
	wc = 1
	f = 2
	tot_time = 0

	while tot_time < min(results):
		fc = c/f
		wc = x/f

		results.append(tot_time+wc)

		tot_time += fc
		f += sf
	print "Case #%d: %f" % (problem+1, min(results))
