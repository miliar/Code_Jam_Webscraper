import math

def calc(numOfStalls, numOfPeople):
    stalls = [numOfStalls];
    for i in range(0, numOfPeople):
        index = 0
        maxValue = 0

        # find largest in leave nodes
        for j in range(0, len(stalls)):
            if (stalls[j] > maxValue):
                maxValue = stalls[j]
                index = j

        divBy2 = maxValue / 2
        isEven = maxValue % 2 == 0
        ls = int(divBy2 - 1) if isEven else int(math.floor(divBy2))
        rs = int(divBy2) if isEven else int(math.floor(divBy2))

        stalls.remove(maxValue)
        stalls.insert(index, ls)
        stalls.insert(index + 1, rs)

    # print("ls", ls, "rs", rs)
    sMax = ls if (ls > rs) else rs
    sMin= ls if (ls < rs) else rs
    return sMax, sMin


with open('C-small-1-attempt0.in.txt') as f:
    data = f.read().split("\n")

    for i in range(1, int(data[0]) + 1):
        row = data[i].split()
        numOfStalls = int(row[0])
        numOfPeople = int(row[1])

        sMax, sMin = calc(numOfStalls, numOfPeople)
        print("Case #{}: {} {}".format(i, sMax, sMin))

    # i = 3
    # row = data[i].split()
    # numOfStalls = int(row[0])
    # numOfPeople = int(row[1])
    # calc(numOfStalls, numOfPeople)
    # sMax, sMin = calc(numOfStalls, numOfPeople)
    # print("Case #{}: {} {}".format(i, sMax, sMin))