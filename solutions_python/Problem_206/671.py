cases = int(raw_input())

for case in range(cases):

	D, N = [int(i) for i in raw_input().split()]

	horses = []

	for i in range(N):
		K, S = [int(i) for i in raw_input().split()]
		horses.append((K, S))

	slowestHorse = -1
	for horse in horses:
		K, S = horse
		#print "D = %s, K = %s, S = %s" % (D, K, S)
		
		timeItTakesInHours = float(D - K) / float(S)
		#print "timeItTakesInHours = %s" % (timeItTakesInHours)

		if timeItTakesInHours > slowestHorse:
			slowestHorse = timeItTakesInHours

	#print "Hours: " + str(slowestHorse)

	answer = str(float(D) / float(slowestHorse))
	

	print "Case #" + str(case+1) + ": " + str(answer)