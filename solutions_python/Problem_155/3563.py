
def solve(data):
	original = list(data)
	maxShy = original[0]
	shylist = [ int(x) for x in original[2:] ]

	invited = 0
	standup = 0

	for shy, num in enumerate(shylist):
		if shy <= standup:
			standup += num
		elif num != 0:
			invited += (shy-standup)
			standup += (num + invited)
	return invited

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		data = raw_input()
		print("Case #%i: %s" % (caseNr, solve(data)))