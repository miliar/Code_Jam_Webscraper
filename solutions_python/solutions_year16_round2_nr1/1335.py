import sys

def getUniqueNumbers(inStr):
    uniqueNums = []
    
    if "Z" in inStr:
        numOfOccurrences = inStr.count("Z")
        for _ in range(0, numOfOccurrences):
            uniqueNums.append(0)
            for c in "ZERO":
                inStr.remove(c)

    if "W" in inStr:
        numOfOccurrences = inStr.count("W")
        for _ in range(0, numOfOccurrences):
            uniqueNums.append(2)
            for c in "TWO":
                inStr.remove(c)

    if "U" in inStr:
        numOfOccurrences = inStr.count("U")
        for _ in range(0, numOfOccurrences):
            uniqueNums.append(4)
            for c in "FOUR":
                inStr.remove(c)

    if "X" in inStr:
        numOfOccurrences = inStr.count("X")
        for _ in range(0, numOfOccurrences):
            uniqueNums.append(6)
            for c in "SIX":
                inStr.remove(c)

    if "G" in inStr:
        numOfOccurrences = inStr.count("G")
        for _ in range(0, numOfOccurrences):
            uniqueNums.append(8)
            for c in "EIGHT":
                inStr.remove(c)

    return uniqueNums, inStr


def getNonUniqueNums(inStr):
    """ 1, 3, 5, 7, 9.

    After removing the unique numbers, we can directly resolve this
    """
    uniqueNums = []
    
    while len(inStr) != 0: 
        if "O" in inStr:
            numOfOccurrences = inStr.count("O")
            for _ in range(0, numOfOccurrences):
                uniqueNums.append(1)
                for c in "ONE":
                    inStr.remove(c)

        if "T" in inStr:
            numOfOccurrences = inStr.count("T")
            for _ in range(0, numOfOccurrences):
                uniqueNums.append(3)
                for c in "THREE":
                    inStr.remove(c)

        if "F" in inStr:
            numOfOccurrences = inStr.count("F")
            for _ in range(0, numOfOccurrences):
                uniqueNums.append(5)
                for c in "FIVE":
                    inStr.remove(c)

        if "S" in inStr:
            numOfOccurrences = inStr.count("S")
            for _ in range(0, numOfOccurrences):
                uniqueNums.append(7)
                for c in "SEVEN":
                    inStr.remove(c)

        if "I" in inStr:
            numOfOccurrences = inStr.count("I")
            for _ in range(0, numOfOccurrences):
                uniqueNums.append(9)
                for c in "NINE":
                    inStr.remove(c)

    return uniqueNums, inStr



def findPhoneNumber(inStr):
    uniqueNums, inStr = getUniqueNumbers(inStr)
    nonUniqueNums, inStr = getNonUniqueNums(inStr)

    assert len(inStr) == 0

    phoneNumber = uniqueNums + nonUniqueNums
    phoneNumber.sort()
    return "".join(str(x) for x in phoneNumber)

def main():
    ln = 0
    T = None
    for line in sys.stdin:
        if ln == 0:
            T = int(line)
            ln += 1
        else:
            inStr = line.rstrip()
            sol = findPhoneNumber(list(inStr))
            print("Case #{0}: {1}".format(ln, "".join(sol)))
            ln += 1

if __name__ == '__main__':
    main()