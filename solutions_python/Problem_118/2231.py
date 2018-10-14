import math

  
def isPalin(num):
    string = str(num)
    return string == string[::-1]

def isSquarePalin(num):
    intOfRoot = int(math.sqrt(num))
    isSquare = num == intOfRoot * intOfRoot
    return isSquare and isPalin(intOfRoot)
    
def isFairAndSquare(num):
    return isPalin(num) and isSquarePalin(num)

def main():
    fh = open("input.txt", 'r')
    output = open("output.txt", 'w')
    numCase = int(fh.readline())

    for eachCase in range(0,numCase):
        thisCase = fh.readline()
        string = thisCase.split()
        startNum = int(string[0])
        endNum = int(string[1])
        fairSqCount = 0
        for eachInt in range(startNum, endNum + 1):
            if isFairAndSquare(eachInt):
                fairSqCount += 1

        output.write("Case #")
        output.write(str(eachCase+1))
        output.write(": ")
        output.write(str(fairSqCount))
        output.write('\n')
        
    fh.close()
    output.close()

main()


