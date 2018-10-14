def solve(infile, outfile):
	f = open(infile, 'r')
	f.readline()
	sets = [ tuple(map(float,line.replace('\n', '').split(" "))) for line in f.readlines()]
	f.close()

	answers = []
	for (C, F, X) in sets:
		interest = 2.0 # interest per second
		time_spend = 0.0

		while True:
			# Suppose we just wait...
			wait_time = X  / interest
			# print "wait:", wait_time

			# Suppose we buy this one time, and then wait...
			buy_time = C / interest
			interest_after_buy = interest + F
			wait_time_after_buy = X / interest_after_buy

			wait_time_with_one_but = buy_time + wait_time_after_buy
			# print "Buy+wait:", wait_time_with_one_but

			# Now make a decision:
			if wait_time < wait_time_with_one_but: # It is best to just wait...
				time_spend += wait_time 
				break
			else: # Best to buy
				time_spend += buy_time
				interest += F
		answers.append(time_spend)

	f = open(outfile, 'w')
	for i in xrange(len(answers)):
		f.write("Case #" + str(i+1) + ": " + str(answers[i]) + "\n")
	f.close()





if __name__ == "__main__":
	import sys

	if not len(sys.argv) == 2:
		print "python solver.py input output"
		sys.exit()

	solve(sys.argv[1]+".in", sys.argv[1]+".out")
