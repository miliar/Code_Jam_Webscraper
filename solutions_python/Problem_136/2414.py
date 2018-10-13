import sys
f = open(sys.argv[1])

cases = int(f.readline())

for case in range(0, cases):
	#print case
	values = [float(x) for x in f.readline().split(' ')]
	(farmcost, productionrate, winning) = values
	#print 'fcost', farmcost, 'rate', productionrate, 'win', winning
	# C farmcost		500
	# F productionrate	4
	# X winning			2000

	#cookies = 0.0

	cps = 2.0 # cookies per second
	time = 0.0
	while(True):
		#should we buy another farm or not?
		#time_to_buy = 

		# winning vs cookies
		# how to get winning?
		time_to_wait = (winning / cps) #- cookies
		time_to_farm = (farmcost / cps) #- cookies

		#print
		#print 'time', time
		#print '2wait', time_to_wait, '2farm', time_to_farm

		if time_to_wait < (time_to_farm + winning / (cps + productionrate)):
			time = time + time_to_wait
			# we won!!!!!!!!!!!!!!!!!
			break
		else:
			# buy another farm when time_to_farm has passed
			time = time + time_to_farm
			cps = cps + productionrate
			#print 'buying farm after', time_to_farm
			#print 'cps', cps
			#break
		#sys.stdin.readline()

	#print 'WON!!!', time
	#print a,b,c
	print 'Case #%d:' % (case+1), time


f.close()
