#textFile = open("test.txt", "w")
textFile = open("output_large.txt", "w")
#textFile = open("output_small.txt", "w")
#open and read the input file
#sInputFileLoc = 'test.in'
sInputFileLoc = 'A-large.in'
#sInputFileLoc = 'A-small-attempt1.in'
sInputFile = open(sInputFileLoc)
sLineOutput = "Case #"
iLineRead = 0
Shyness = []
iShynessMax = 0

#Import the first line of the file. The first line contains how many different test cases are in the file being imported
iNumTestCases = int(sInputFile.readline())
for x in range(iNumTestCases):
        sInputString = sInputString = sInputFile.readline()
        Shyness = sInputString.split(' ', 1)
        iShynessMax = Shyness[0]
        audienceLevels = list(Shyness[1])
        audienceLevels.remove('\n')
        
        iPersonCount = 0
        iFriendCount = 0
        for z in range(len(audienceLevels)):
                if z == 0:
                        iPersonCount = int(audienceLevels[0])
                else:
                        if iPersonCount <= z:
                                iFriendCount = iFriendCount + (z - iPersonCount)
                                iPersonCount = iPersonCount + int(audienceLevels[z]) + (z - iPersonCount) 
                        else:
                                iPersonCount = iPersonCount + int(audienceLevels[z])                       
        textFile.write('Case #' + str(x + 1 ) + ': ' + str(iFriendCount)+"\n")

textFile.close()

