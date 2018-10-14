'''
Created on May 7, 2011

@author: minhluong
'''

inputFile = open("A-large.in", "r")
outputFile = open("output.txt", "w")

testsNum = int(inputFile.readline().rstrip('\n')) #get number of test cases
testIndex = 1

while (testIndex <= testsNum): # for each test case
    outputFile.write("Case #{0:1d}:\n".format(testIndex))
    
    R, C = [int(x) for x in inputFile.readline().rstrip('\n').split(' ')]
    
    tiles = [""]*R
    for i in range(R):
        tiles[i] = inputFile.readline().rstrip('\n')

    impossible = False
    for i in range(R):
        if (impossible):
            break
        for j in range(C):
            if (tiles[i][j] == "#"):
                if (i<R-1 and j<C-1 and tiles[i][j+1] == "#" and tiles[i+1][j] == "#" and tiles[i+1][j+1] == "#"):
                    tiles[i] = tiles[i][:j] + "/" + tiles[i][j+1:]
                    tiles[i+1] = tiles[i+1][:j] + '\\' + tiles[i+1][j+1:]
                    tiles[i] = tiles[i][:j+1] + '\\' + tiles[i][j+2:]
                    tiles[i+1] = tiles[i+1][:j+1] + "/" + tiles[i+1][j+2:]
                else:
                    impossible = True
                    break
    
    if (impossible):
        outputFile.write("Impossible\n")
    else:
        for i in range(R):
            outputFile.write("{0:s}\n".format(tiles[i]))
#            print tiles[i]
    
    print
    testIndex += 1

inputFile.close()
outputFile.close()

if __name__ == "__main__":
    pass