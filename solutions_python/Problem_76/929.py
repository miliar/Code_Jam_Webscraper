'''
Created on May 7, 2011

@author: minhluong
Google Code Jam 2011
Problem 1C: Candy Splitting
'''

inputFile = open("C-large.in", "r")
outputFile = open("output.txt", "w")

testsNum = int(inputFile.readline().rstrip('\n')) #get number of test cases
testIndex = 1
while (testIndex <= testsNum):
    numCandy = int(inputFile.readline().rstrip('\n'))
    candies = inputFile.readline().rstrip('\n').split(' ')

    xor = 0
    min = 999999999
    sum = 0
    for i in range(numCandy):
        candies[i] = int(candies[i])
        xor ^= candies[i]
        sum += candies[i]
        if (min > candies[i]):
            min = candies[i]
    
    if (xor != 0):
        outputFile.write("Case #{0:1d}: NO\n".format(testIndex))
    else:
        outputFile.write("Case #{0:1d}: {1:1d}\n".format(testIndex, sum-min))
    testIndex += 1

inputFile.close()
outputFile.close()

if __name__ == '__main__':
    pass