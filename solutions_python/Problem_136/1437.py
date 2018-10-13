inputFile = open("B-large.in", 'r')

count =  int(inputFile.readline())

for y in range(1, count+1):
    currentRate = 2.0
    totalSeconds = 0.0
    price, boost, winCount = [float(f) for f in inputFile.readline().split()]

    doneFinding = False

    while not doneFinding :
        noBuySeconds = winCount/currentRate
        newBuyRate = currentRate + boost
        if noBuySeconds > ((price/currentRate) + (winCount/newBuyRate)):
            totalSeconds += (price/currentRate)
            currentRate = newBuyRate
        else:
            totalSeconds += noBuySeconds
            doneFinding = True

    print "Case #%s:" % y, totalSeconds