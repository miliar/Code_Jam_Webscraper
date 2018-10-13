import fileinput

input = fileinput.input()
rl = lambda : input.readline()
count = int(input.readline())
cases = [map(float, rl().split()) for l in range(count)]

def time_it(C, F, X):
	c_ps = 2.0
	eta = lambda c_ps : X / float(c_ps)
	rate_arr = []
	time_spent = sum(rate_arr)
	while time_spent + eta(c_ps) > time_spent + C/c_ps + eta(c_ps+F):
		rate_arr.append(C/c_ps)
		c_ps += F
	return sum(rate_arr) + eta(c_ps)

for i,case in enumerate(cases):
	print "Case #%d: %.7f" % (i+1, time_it(*case))