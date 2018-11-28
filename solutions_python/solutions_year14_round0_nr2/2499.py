import sys

def main():
	std_input = sys.stdin.read().split('\n')

	no_test_cases = int(std_input.pop(0))

	f = open('output.txt', 'w')

	for i in range(no_test_cases):
		info = std_input.pop(0).split()
		
		farmPrice = float(info[0])
		extraCookiesPerSecond = float(info[1])
		winningCookieNumber = float(info[2])

		f.write("Case #" + str(i + 1) + ": " + determineResult(farmPrice, extraCookiesPerSecond, winningCookieNumber) + '\n')

	f.close()


def determineResult(farmPrice, extraCookiesPerSecond, winningCookieNumber):
	currentCookiesPerSecond = 2
	currentCookies = 0
	timeTaken = 0
	
	cont = False

	while cont == False:
		timeToWin = winningCookieNumber/currentCookiesPerSecond
	
		timeToGetFarm = farmPrice/currentCookiesPerSecond

		timeToWinIfBuyFarmToo = timeToGetFarm + (winningCookieNumber/(currentCookiesPerSecond + extraCookiesPerSecond))
		
		if timeToWin < timeToWinIfBuyFarmToo:
			return str(timeToWin + timeTaken)
			cont = True
		else:
			timeTaken += timeToGetFarm
			currentCookiesPerSecond += extraCookiesPerSecond


if __name__ == "__main__":
	main()
