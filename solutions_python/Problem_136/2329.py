ipt = open('B-large.in').read().splitlines()
cases = int(ipt[0])


fw = open('B-large.out','w')
for i in xrange(cases):
	c_per_sec = 2.0
	c,f,x = map(lambda x: float(x), ipt[i+1].split(' '))

	just_wait = x / c_per_sec

	sub_total = 0
	while True:
		#print just_wait
		sub_total += c/c_per_sec
		c_per_sec += f
		total = sub_total + (x / c_per_sec)

		if total >= just_wait:
			fw.write("Case #{}: {}\n".format(i+1, round(just_wait, 7)))
			break
		else:
			just_wait = total
fw.close()