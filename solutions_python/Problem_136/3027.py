lines = [line.strip() for line in open('/Users/jlinenthal/downloads/B-large.in')]

n = int(lines[0])
idx=1
for i in range(1,n+1):
    C = map(float, lines[i].split(' '))[0]
    F = map(float, lines[i].split(' '))[1]
    X = map(float, lines[i].split(' '))[2]
    #print C,F,X
    curRate = 2.0
    curCookies = 0
    t = 0.0
    while True:
	timeToWinBuyFarm = (X / (curRate + F)) + (C/curRate)
	timeToWinCur = (X / curRate)
	#print timeToWinBuyFarm, timeToWinCur
	if timeToWinCur < timeToWinBuyFarm:
	    print 'Case #' + str(i) + ': ' + str(t+timeToWinCur)
	    break;
	else:
	    t += C/curRate
	    curRate += F
