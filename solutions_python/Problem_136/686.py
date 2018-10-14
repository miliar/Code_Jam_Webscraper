#
# Google Code Jam 2014
# Problem B: Cookie Clicker Alpha
# 
# Solved by Michael Oliver (a.k.a. The Code Boss)
# April 11, 2014
#

import sys
sys.setrecursionlimit(10000)

# Helpers
CookiesPerSecond = 2.0

def TimeToGetXCookies(NumCookies, NumFarms, C, F, X):
	return (X - NumCookies) / (CookiesPerSecond + F*NumFarms)
	
def TimeToNextFarm(NumCookies, NumFarms, C, F, X):
	return TimeToGetXCookies(NumCookies, NumFarms, C, F, C)
	
def FindOptimalTime(NumCookies, NumFarms, C, F, X):
	Time = 0.0
	while True:
		t1 = TimeToGetXCookies(NumCookies, NumFarms, C, F, X)
		t2 = TimeToNextFarm(NumCookies, NumFarms, C, F, X)
		if t1 < t2:
			return Time + t1
		else:
			t3 = t2 + TimeToGetXCookies(NumCookies, NumFarms+1.0, C, F, X)
			if t1 < t3:
				return Time + t1
			else:
				Time += t2
				NumFarms += 1.0

# Main program
NumTests = int(input())

for TestNumber in range(1,NumTests+1):

	C, F, X = map(lambda x: float(x), input().split())
	
	NumCookies = 0.0
	NumFarms = 0.0
	
	Time = FindOptimalTime(NumCookies, NumFarms, C, F, X)
	
	print('Case #%d: %f' % (TestNumber, Time))