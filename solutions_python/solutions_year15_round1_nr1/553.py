with open("A-large (1).in","r") as f:
    numOfCase = int(f.readline())
    print(numOfCase)
    for i in range(numOfCase):
        firstAnswer = 0
        secondAnswer = 0
        rate = 0
        numPlate = int(f.readline())
        lists = f.readline().split()
        lists = list(map(int,lists))
        for l in range(numPlate):
            if (l > 0):
                if (rate < lists[l-1]-lists[l]):
                    rate = lists[l-1]-lists[l]
        for j in range(numPlate):
            if (j > 0):
                if (lists[j] < lists[j-1]):
                    firstAnswer += lists[j-1]-lists[j]
        for k in range(numPlate-1):
            if (lists[k] <= rate):
                secondAnswer += lists[k]
            elif (lists[k] > rate):
                secondAnswer += rate
        print("Case #%d: %d %d" % (i+1,firstAnswer,secondAnswer))
f.closed



