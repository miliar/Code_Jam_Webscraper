def solve(case):
	a = case.split(' ')
	l = int(a[0])
 	vals = a[1]
	audience_standing = 0
	friends=0
	for i in xrange(l+1):
		shyness = i
		if audience_standing < shyness:
			need_more = shyness-audience_standing
			friends+=need_more
			audience_standing+=need_more
		audience_standing += int(vals[i])
	return friends
if __name__ == "__main__":
	testcases = input()
     
	for caseNr in xrange(1, testcases+1):
		print("Case #%i: %s" % (caseNr, solve(raw_input())))
