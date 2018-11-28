import sys
with open('/users/nishanthshanmugham/Downloads/B-large.in') as sys.stdin:

	T = int(sys.stdin.readline())
	for case_n in xrange(T):
		line = sys.stdin.readline().strip()
		table = (line.split(" "))
		C = float(table[0])
		F = float(table[1])
		X = float(table[2])
		Rate = 2 # starts

		TotalTime1 = 0
		TotalTime2 = 0

		while (not((X/Rate) < (X)/(Rate+F) + C/Rate)):
			TempTotalTime2 = X / Rate
			TempTotalTime1 = C / Rate
			TotalTime1 = TotalTime1 + TempTotalTime1
 			Rate = Rate + F
 			#print (TotalTime1, Rate)

		#TotalTime1 = TotalTime1 + TempTotalTime1
		TotalTimeFinal = TotalTime1 + X/Rate
		print "Case #%d: %.7f" % (case_n+1, TotalTimeFinal)

