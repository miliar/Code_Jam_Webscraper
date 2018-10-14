from decimal import *
#getcontext().prec = 7

F = open('B-small-attempt0.in').read()

f = F.split('\n')
T = f[0]

for t in range(0,int(T)):
	r = f[t+1].split()
	C = float(r[0]) # farm cost
	F = float(r[1]) # farm bonus
	X = float(r[2]) # target cookies

	tc = float(0) # total cookies
	ft = float(0) # total farms
	tp = float(2) # total cookie production
	tf = float(0) # time till next farm buyout
	sw = float(0) # seconds to wait to win
	ts = float(0) # total seconds

	minimum = X/tp

	prev = float(minimum) # previous value of sw

	while ts < 600:
		tc += tp

		tf = C/tp
		ts += tf
		tp += F

		sw = X/tp
		if(prev < ts+sw):
			break
		prev = ts+sw
		
	print "Case #%d: %.7f" % (t+1,prev)