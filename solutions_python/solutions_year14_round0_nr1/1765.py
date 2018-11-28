def main():
    numOfIter = int(raw_input())
    for i in xrange(numOfIter):
        (firstArr, secondArr) = parseData()
        inter = firstArr.intersection(secondArr)
        print "Case #%d:" % (i+1),
        if len(inter) == 0:
            print "Volunteer cheated!"
        elif len(inter) == 1:
            print inter.pop()
        else:
            print "Bad magician!"

def parseData():
    firstRow = int(raw_input())
    firstArr = set()
    for i in range(4):
        line = raw_input()
        if i+1 == firstRow:
            [firstArr.add(int(x)) for x in line.split(" ")]
    secondRow = int(raw_input())
    secondArr = set()
    for i in range(4):
        line = raw_input()
        if i+1 == secondRow:
            [secondArr.add(int(x)) for x in line.split(" ")]
    return (firstArr,secondArr)

if __name__ == "__main__":
    main()
