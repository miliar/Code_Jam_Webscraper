def intToList(num):
    return [int(c) for c in str(num)]

def isTiny(num):
    lNb = intToList(num)
    for j in range(0, len(lNb[:-1])):
        if lNb[j] <= lNb[j+1]:
            continue
        else:
            return False
    return True

def getLastTinyNumb(maxNum):
    currentNb = -1

    # One digit
    if maxNum < 10:
        return maxNum
    else:
        for i in range(1, maxNum+1):
            if isTiny(i):
                currentNb = i

    print ("TinyNum: "+str(currentNb))

    return currentNb;

if __name__ == "__main__":

    print ("Google Jam Pb2")

    infile = open("B-small-attempt0.in", "r")
    outfile = open("B-small-attempt0.out", "w")

    t = int(infile.readline())  
    for i in range(1, t + 1):
        l = infile.readline().split(" ")
        print ("MaxNum: "+l[0][:-1]+" Case: "+str(i))
        latestTinyNum = getLastTinyNumb(int(l[0][:-1]))
        print("Case #{}: {}".format(i, latestTinyNum), file = outfile)