'''
Created on May 7, 2011

@author: minhluong
'''

def average(list, myRange, mode):
    count = 0
    sum = 0
    if (mode == 0):
        for i in myRange:
            if (list[i] == -1):
                continue
            count += 1
            if (list[i] == 0):
                continue
            if (list[i] == 1):
                sum += 1
    else:
        for i in myRange:
            count += 1
            sum += list[i]
    return float(sum)/count

inputFile = open("A-large.in", "r")
outputFile = open("output.txt", "w")

testsNum = int(inputFile.readline().rstrip('\n')) #get number of test cases
testIndex = 1

while (testIndex <= testsNum): # for each test case
    outputFile.write("Case #{0:1d}:\n".format(testIndex))

    numTeams = int(inputFile.readline().rstrip('\n'))
    stat = [ [0 for i in range(numTeams)] for i in range(numTeams) ]
    WP = [0.0]*numTeams
    OWP = [0.0]*numTeams
    OOWP = [0.0]*numTeams
    RPI = 0.0
    
    for i in range(numTeams):
        line = inputFile.readline().rstrip('\n')
        for j in range(numTeams):
            if (line[j] == "."):
                stat[i][j] = -1
            elif (line[j] == "0"):
                stat[i][j] = 0
            elif (line[j] == "1"):
                stat[i][j] = 1
    
    for i in range(numTeams):
        newRange = []
        newRange1 = []
        for j in range(numTeams):
            if (stat[i][j] != -1 and i != j):
                newRange.append(j)
            if (i != j):
                newRange1.append(j)
        for j in newRange1:
            WP[j] = average(stat[j], newRange1, 0)
        OWP[i] = average(WP, newRange, 1)
        print newRange, OWP[i]
        
    for i in range(numTeams):
        newRange = []
        for j in range(numTeams):
            if (stat[i][j] != -1 and i != j):
                newRange.append(j)
        OOWP[i] = average(OWP, newRange, 1)
        
    for i in range(numTeams):
        RPI = 0.25*average(stat[i], range(numTeams), 0) + 0.5*OWP[i] + 0.25*OOWP[i]
        print RPI
        outputFile.write("{0:0.12f}\n".format(RPI))
    
#    print WP
#    print OWP
    print OOWP
    print
    
    
    testIndex += 1

inputFile.close()
outputFile.close()

if __name__ == "__main__":
    pass