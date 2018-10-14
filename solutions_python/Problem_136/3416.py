def GetTime(C, F, X, farms):
    timer = 0
    farmCounter = 0
    currentSpeed = 2
    while (farmCounter < farms):
        timer = timer + C/currentSpeed
        currentSpeed = currentSpeed + F
        farmCounter = farmCounter + 1
    timer = timer + X/currentSpeed
    return timer

def GetBestTime(testCase):
    C = float(testCase[0])
    F = float(testCase[1])
    X = float(testCase[2])
    currentBest = 99999999999999.0
    counter = 0
    while (True):
        currentTime = GetTime(C, F, X, counter)
        counter = counter + 1
        if currentBest >= currentTime:
            currentBest = currentTime
        else:
            return currentBest
    
def main():
    f = open('B-small-attempt0.in', 'r')
    o = open('B-small-attempt0.out','w')
    limit = f.readline()
    
    for i in range(int(limit)):
        testCase = f.readline()
        testCase = testCase[:-1].split(' ')
        answer = GetBestTime(testCase)
        o.write("Case #" + str(i+1) + ": " + "{0:.7f}".format(answer) + "\n")
    o.close()
    f.close()