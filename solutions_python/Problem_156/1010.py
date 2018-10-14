from math import ceil
T = int(raw_input())

def getbesttime(add, l):
	# if we do not divide
	besttime = add + l[0]
	
	# try to divide the biggest pile
	if l[0] <= 3:
		return besttime
	prevtime = besttime
	for take in xrange(int(ceil(0.5*l[0])),1,-1):
		newl = l[:]
		newl[0] -= take
		newl.append(take)
		newl.sort(reverse=True)
		testtime = getbesttime(add+1, newl)
		if testtime < besttime:
			besttime = testtime
		if testtime > prevtime:
			break
		prevtime = testtime
	return besttime

for case in xrange(T):
	D = int(raw_input())
	plates = map(int, raw_input().strip().split())
	plates.sort(reverse=True)
	#print
	#print D,'diners',plates
	
	print 'Case #'+str(case+1)+':',getbesttime(0,plates)
