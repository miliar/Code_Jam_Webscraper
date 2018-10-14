#!/usr/bin/python

import sys

if len(sys.argv) != 2:
	print sys.argv[0], '<input file>'
	sys.exit(1)

fin = open(sys.argv[1], 'r')

cases = int(fin.readline().strip())

for case in range(0, cases):
	#print 'Case #' + `case+1` + ':'
	print 'Case #' + `case+1` + ':',
	cost,farm,target = fin.readline().strip().split(' ')

	cost = float(cost)
	farm = float(farm)
	target = float(target)

	#print '  cost:' + `cost`, 'farm:' + `farm`, 'target:' + `target`

	rate = 2
	now = 0
	time = 0

	#print '  rate:' + `rate`, 'now:' + `now`, 'time:' + `time`

	while now < target:
		# Pre-check, wait until target or wait until upgrade
		timeToTarget = (target - now) / rate

		if cost > target:
			#print '  Just wait'
			time += timeToTarget
			break

		# Wait until upgrade
		timeToUpgrade = (cost - now) / rate

		now = cost
		time += timeToUpgrade

		# Choices, upgrade or wait
		timeToTarget = (target - now) / rate
		timeToTargetAfterUpgrade = target / (rate + farm)

		#print ' ', timeToTarget, timeToUpgrade, timeToTargetAfterUpgrade

		if timeToTarget < timeToTargetAfterUpgrade:
			#print '  Should wait'
			time += timeToTarget
			break

		#print '  Upgraded'
		rate += farm
		now = 0
		#print '  rate:' + `rate`, 'now:' + `now`, 'time:' + `time`

	#print ' ', time
	print time
