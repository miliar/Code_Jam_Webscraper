import sys

cases = int(raw_input())

for c in xrange(cases):
	C,F,X = map(float, raw_input().split())
	
	num_factories = 2000
	
	time_for_factory = [sys.maxint * 100]
	
	rates = [2.0] + [i*F+2.0 for i in xrange(1,num_factories)] # 100 factories
	
	rate_times = map(lambda x: C/x, rates)

	times_to_X = [X/2.0] # the start rate
	
	for i in xrange(1,num_factories):
		times_to_X.append(sum(rate_times[0:i]) + X/(rates[i]))
	
	print "Case #%d: %.7f" % (c+1, min(times_to_X))