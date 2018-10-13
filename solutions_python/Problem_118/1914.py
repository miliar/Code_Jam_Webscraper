def isPalin(number):
    """
    returns True of False is number is palindrom
    """
    if(str(number)[::-1].__eq__(str(number))):
        return True
    return False

def sqList(numList):
    """
    return the square of number list
    """
    numList = map(lambda x : x**2, numList)
    return numList

def fSquare(sqlist, numlist):
    """
    Fair and Square number
    """
    import math, numbers
    i = 0
    counter = 0
    while i < len(numlist):
        if isPalin(numlist[i]):
            if int(math.sqrt(numlist[i]))**2 == int(numlist[i]):
                if isPalin(int(math.sqrt(numlist[i]))):
                    counter += 1
        i += 1
    return counter

def main():
    """
    file read write function
    """
    inFile = open("C.in", "r")
    cases = int(inFile.readline())
    cases += 1
    i = 1
    while i < cases:
        numRange = map(long, inFile.readline().split())

        numlist = range(numRange[0],numRange[1]+1)
        sqlist = sqList(numlist)

        casecounter = fSquare(sqlist, numlist)

        outFile = open("C.out", "a")
        outWrite = "Case #%d: %d\n" % (i, casecounter)
        outFile.write(outWrite)
        outFile.close()

        i += 1
    inFile.close()
if __name__ == "__main__":
    main()