import sys

sys.setrecursionlimit(1000000)
fileName = sys.argv[1]
def main():
	with open(fileName) as FileReader:
		testCases = int(FileReader.readline())
		for caseIndex in range(1, testCases + 1):
			parameter = [float(x) for x in FileReader.readline().split()]
			C = float(parameter[0])
			F = float(parameter[1])
			X = float(parameter[2])
			cookieRate = 2.0
			cookies = 0.0
			time = 0.0
			print("Case #%i: %.7f" % (caseIndex, recurse(C, F, X, cookieRate, cookies, time)))

def recurse(C, F, X, cookieRate, cookies, time):
	if X - cookies > C:
		newTime = ((C - cookies) / cookieRate) + time
		newCookieRate = cookieRate + F
		newCookies = cookies + (newTime - time) * cookieRate - C
		if time + (X - cookies) / cookieRate > newTime + (X - newCookies) / newCookieRate:
			return recurse(C, F, X, newCookieRate, newCookies, newTime)
		else:
			return time + (X - cookies) / cookieRate
	else:
		return time + (X - cookies) / cookieRate


main()