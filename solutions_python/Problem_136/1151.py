
INPUT_FILE = 'cookieInput.txt'
OUTPUT_FILE = 'cookieOutput.txt'

def cookieFunction():
    inputFile = open(INPUT_FILE, 'r')
    outputFile = open(OUTPUT_FILE, 'w')
    noTestCase = int(inputFile.readline())

    for i in xrange(noTestCase):
        outputLine =  "Case #" + str(i+1) + ": "
        theLine = inputFile.readline()
        
        #get variable C, F and X
        variable = []
        count = 0
        while len(variable) < 3:
            word = ""
            while theLine[count] != " " and theLine[count] != "\n":
                word += theLine[count]
                count += 1
            else:
                variable.append(word)
            count += 1

        C = float(variable[0])
        F = float(variable[1])
        X = float(variable[2])
        
        timeTaken = computeShortestTime(C, F, X)
        
        outputLine += str(timeTaken)
        outputFile.write(outputLine + '\n')


def computeShortestTime(C, F, X):
    cps = 2
    time1 = X/2
#    time2 = X/2-1
    farm = 0
    timeToEarnFarms = 0

#    while time1 > time2:
#        time1 = time2
#        farm += 1
#        timeToEarnFarms += C/cps
#        cps += F
#        time2 = X/cps + timeToEarnFarms
#    
#    if (farm-1) == 0:
#        time1 = X/2

    while True:
        farm += 1
        timeToEarnFarms += C/cps
        cps += F
        time2 = X/cps + timeToEarnFarms
        if time1 < time2:
            break
        else:
            time1 = time2


    
    return round(time1,7)

if __name__ == '__main__':
    cookieFunction()