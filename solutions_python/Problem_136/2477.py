import sys
sys.stdin = open('i.txt')
sys.stdout = open('o.txt','wb')
imap = lambda x: map(int,x.strip().split())
fmap = lambda x: map(float,x.strip().split())
def getinput(callback=lambda x: x):
	return callback(raw_input())
def simulate(caseNumber):
	c,f,x = getinput(fmap)
	rate = 2;	
	totalTime = 0;
	while 1:
		timeToWinWithCurrentProduction = float(x) / rate;
		timeToBuyNewFactory = (float(c) / rate)
		timeToWinWithIncreasedProduction = (float(x) / (rate + f)) + timeToBuyNewFactory		
		if timeToWinWithIncreasedProduction < timeToWinWithCurrentProduction: 
			rate += f;			
			totalTime += timeToBuyNewFactory;
		else:
			totalTime += timeToWinWithCurrentProduction;
			break;
	print 'Case #%i: %.7f' % (caseNumber+1,totalTime)	
def main():
	tc = getinput(int)
	for caseNumber in xrange(tc):
		simulate(caseNumber)
main()