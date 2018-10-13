import glob, time, string, re, math

#textFile = open("test.txt", "w")
#textFile = open("output_large.txt", "w")
textFile = open("output_small.txt", "w")
#open and read the input file
#sInputFileLoc = 'test.in'
#sInputFileLoc = 'C-large-practice.in'
sInputFileLoc = 'C-small-attempt0.in'
sInputFile = open(sInputFileLoc)
sLineOutput = "Case #"
iLineRead = 0


def sqrt(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1
        if ans*ans != x:
            #print (x, 'is not a perfect square.')
            return None
        else:
            #print (x, ' is a perfect square.')
            return ans
    else:
        #print (x, ' is not a positive number.')
        return None

iSquareNumbers = [x*x for x in range(10000)]

iPalindome = []
def palindrome(x):
    return str(x) == str(x)[::-1]

for x in range(10000):
    if palindrome(x) == True:
        iPalindome.append(x)
iCombinedList = sorted(set(iPalindome) & set(iSquareNumbers))

#print(iCombinedList)

#final list of numbers that are both
iFinalList= []

for x in iCombinedList:
    y = sqrt(x)
    if y in iPalindome:
        iFinalList.append(x)
print(iFinalList)






#Import the first line of the file. The first line contains how many different test cases are in the file being imported
iNumTestCases = int(sInputFile.readline())

#based on the numer of test cases in the first line, loop through these each one by one
for x in range(iNumTestCases):
    #import the first line of text
    sInputString = sInputFile.readline()
    sInputString = sInputString.split()
    #separate out the items into an array
    sTemp = ""
    sTempLast = ""
    count = 0
    #print(sInputString)
    
    for z in iFinalList:
        if z >= int(sInputString[0]) and z <= int(sInputString[1]):
            count += 1
    #print(count)
    textFile.write(sLineOutput+str(x+1)+ ": " +str(count)+"\n")
    textFile.write(sTemp)
    sTempLast = ""

textFile.close()
#115 - 200 done

