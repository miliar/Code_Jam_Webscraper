"""Resolution really simple
Loop : 
	Calcul the time last if you don't buy farm anymore
	Calcul the time needed to buy the next farm 
	If the time needed to buy the next farm is less then the time needed to finish, consider buying
		if we buy, add the time needed to buy the farm, increment the gain and loop again !
"""


def solve(Cost, Finv, Xgoal):
	# print Cost, Finv, Xgoal
	gainactuel = 2.0
	time = 0
	# init 


	while True:
		timelast = Xgoal / gainactuel # time to win
		timetobuy = Cost / gainactuel # time to buy the farm
		timelastifbuy = timetobuy + Xgoal / (gainactuel + Finv)
		#print "timelast", timelast
		#print "timelastifbuy", timelastifbuy
		if timetobuy < timelast and timelastifbuy < timelast:
			# Buy !
			time += timetobuy
			gainactuel += Finv
		else:
			# add the time last
			time += timelast
			time = round(time, 7)
			return str(time)


fr = open('B-large.in', 'r')
fw = open('output.txt', 'w+')
numcases = int(fr.readline())
idline = 0

for x in xrange(1,numcases+1):
	idline += 1
	inputs = fr.readline().replace('\n', '').split(' ')
	finputs = [float(inputr) for inputr in inputs]
	time = solve(*finputs)
	fw.write("Case #"+str(idline)+": "+str(time)+'\n')