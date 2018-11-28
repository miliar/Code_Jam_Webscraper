def process(intermediate, acceleration, finalCount):
	rate = 2
	ts = 0.0
	while(True):		
		temp1 = finalCount/rate
		temp2 = intermediate/rate + finalCount/(rate+acceleration)
		if temp2 > temp1:
			break		
		ts += (intermediate/rate)	
		rate = rate+acceleration		
	ts += temp1
	return ts
	

noTestCases = int(raw_input())
caseNo = 0
while(noTestCases > 0):
	caseNo +=1
	ip = raw_input()
	ip = ip.split()
	C = float(ip[0])
	F = float(ip[1])
	X = float(ip[2])
	op = process(C, F, X)
	print "case #%d: %.7f" %(caseNo, op)
	noTestCases -= 1	