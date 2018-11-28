import fileinput
def solve(plates):
	minutes = max(plates)
	for bigplate in range(1, max(plates) + 1):
		minutes = min(minutes, splitdownto(bigplate, plates))
	return minutes

def splitdownto(eat, ps):
	plates = list(ps)
	i = 0
	splits = 0
	while i < len(plates):
		if plates[i] > eat:
			plates.append(plates[i] - eat)
			plates [i] = eat
			splits+=1
		i+=1
	return splits + max (plates)
 
lines = fileinput.input()
testcases = int(lines.readline())
   
for caseNr in range(1, testcases+1):
    diners = int(lines.readline())
    pancakestring = lines.readline()
    pancakelist = [int(x) for x in list(pancakestring.split(" "))]
    print("Case #%i: %i" % (caseNr, solve(pancakelist)))

