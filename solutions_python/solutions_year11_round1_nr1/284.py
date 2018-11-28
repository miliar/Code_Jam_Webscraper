'''
Created on May 7, 2011

@author: minhluong
'''

inputFile = open("A-small-attempt2.in", "r")
outputFile = open("output.txt", "w")

testsNum = int(inputFile.readline().rstrip('\n')) #get number of test cases
testIndex = 1

while (testIndex <= testsNum): # for each test case
    inputNum = inputFile.readline().rstrip('\n').split(' ')
    maxToday = int(inputNum[0])
    percentToday = int(inputNum[1])
    percentTotal = int(inputNum[2])
    wonToday = 0
    
    solved = False
    
    if (percentToday != 0 and percentTotal == 100):
        outputFile.write("Case #{0:1d}: {1}\n".format(testIndex, "Broken"))
    
    print maxToday, percentToday, percentTotal
    
    for i in range(1, maxToday+1):
        if (i*percentToday/100 == i*percentToday/100.):
            wonToday = i*percentToday/100
#            print "i is", i # i is one of the possible number of games played today
            if (percentToday == percentTotal):
                outputFile.write("Case #{0:1d}: {1}\n".format(testIndex, "Possible"))
                solved = True
                break
            
            totalPlayedBefore = 1
            while (totalPlayedBefore < 3000):
                for x in range(totalPlayedBefore+1):
#                    print ((wonToday + x)/(i + totalPlayedBefore+0.0))
                    if ( ((wonToday + x)/(i + totalPlayedBefore+0.0)) == percentTotal/100.):
                        outputFile.write("Case #{0:1d}: {1}\n".format(testIndex, "Possible"))
                        solved = True
                        break
                if (solved):
                    break
                totalPlayedBefore += 1
    
    if (solved):
        solved = False
        testIndex += 1
        continue
    
    outputFile.write("Case #{0:1d}: {1}\n".format(testIndex, "Broken"))
    testIndex += 1

inputFile.close()
outputFile.close()


if __name__ == "__main__":
    pass