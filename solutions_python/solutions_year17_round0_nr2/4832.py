

def solve(n):
	for num in xrange(n, 0, -1):
		digits = [int(i) for i in str(num)]
		found = True
		for i in range(len(digits)-1):
			if digits[i] > digits[i+1]: 		
				found = False
				break
		if found is True:
			return num

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        N = int(raw_input())
        print("Case #%i: %s" % (caseNr, solve(N)))


