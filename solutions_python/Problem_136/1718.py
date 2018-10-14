numOfCases = int(raw_input())

def to_infinity():
    index=1
    while 1:
        yield index
        index += 1

for caseNum in range(1, numOfCases+1):
	c, f, x = [float(val) for val in raw_input().split(" ")]

	scenarios = [x/2]
	for i in to_infinity():
		s = 0
		cps = 2
		for fab in range(i):
			t = c / cps
			s += t
			cps += f
		val = s + x/cps
		if val > x/2 or val > min(scenarios):
			break
		else:
			scenarios.append(s + x/cps)
	print "Case #%d: %f" % (caseNum, min(scenarios))

