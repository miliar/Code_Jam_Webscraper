from sys import stdin
from pprint import pprint
readline = stdin.readline

T = int(readline())

for case in range(T):
	(R,k,N) = map(int,readline().split(' '))
	grps = map(int,readline().split(' '))
	loads = [None] * N
	for i in range(N):
		incar,numgrps = (0,0)
		while (incar + grps[(i+numgrps)%N] <= k and numgrps < N):
			incar+=grps[ (i+numgrps)%N ]
			numgrps+=1
		loads[i] = (incar,numgrps)
	
#	print R,k,N						#	DEBUG
#	print grps						#	DEBUG
#	print loads						#	DEBUG
	
	#calculate the cycle point
	beenhere = [False]*N
	here = 0
	while not beenhere[here]:
		beenhere[here] = True
		here = (here + loads[here][1]) % N
#	print "cycle starts at " , here		# DEBUG

	#calculate cycle length and profit
	cyclestart,cyclelength,cyclevalue = here,1,loads[here][0]
	here = (here + loads[here][1]) % N
	while here is not cyclestart:
		cyclelength += 1
		cyclevalue += loads[here][0]
		here = (here + loads[here][1]) % N
#	print "the cycle has length " , cyclelength , " and is worth ", cyclevalue			# DEBUG

	#so what's the profit to get to the first cycle?
	here,tripsleft,dayprofit = 0,R,0
	while tripsleft > 0 and here is not cyclestart:
		tripsleft -= 1
		dayprofit += loads[here][0]
		here = (here + loads[here][1]) % N
#	print "after prefix, we made " , dayprofit , " profit so far, and we have some trips left: ", tripsleft 			# DEBUG

	# use up most of the rides for the day, in this cycle
	numcycles = tripsleft / cyclelength
	tripsleft -= numcycles * cyclelength
	dayprofit += numcycles * cyclevalue
#	print "after cycles, we made " , dayprofit , " profit so far, and we have some trips left: ", tripsleft 			# DEBUG

	# use up leftovers
	while tripsleft > 0:
		tripsleft -= 1
		dayprofit += loads[here][0]
		here = (here + loads[here][1]) % N
#	print "after suffix, we made " , dayprofit , " profit so far, and we have some trips left: ", tripsleft 			# DEBUG

	print "Case #%d: %d" % (case+1, dayprofit)
#	print

