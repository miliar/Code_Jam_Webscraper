import sys

#Runs cookie script
def cookies():
    caseNum = 0
    #Opens input/output stuff
    input = open(sys.argv[1], 'r');
    output = open("Output.txt", 'w');
    #Skip over number of test cases
    input.readline();
    #Read through input file
    for line in input:
        #For each line, extract C, F, X
        cfxList = line.split()
        time = calcTime(float(cfxList[0]),
                        float(cfxList[1]),
                        float(cfxList[2]))
        #Write sum to output
        caseNum += 1
        outLine = "Case #{}: {}\n".format(caseNum,
                                          time)
        output.write(outLine)
    input.close()
    output.close()

#Loop through and calculate sum until sum >= X
def calcTime(c, f, x):
    time, cookieRate = 0.0, 2.0
    min_time = float("inf")
    while (True):
        timeElapsed = x / cookieRate + time
        if (timeElapsed < 0 or timeElapsed >= min_time):
            return min_time
        else:
            min_time = timeElapsed
        time += (c / cookieRate)
        cookieRate += f

cookies()
