def horizontal(lawndim, lawn):
    """
    return all possible horizontal elements
    """
    horizonlSet = []
    i = 0
    while i < lawndim[0]:
        j = 0
        horrow = [] #one row
        while j < lawndim[1]:
            horrow.append(lawn[i][j])
            j += 1
        horizonlSet.append(horrow)
        i += 1
    return horizonlSet

def vertical(lawndim,lawn):
    """
    return all possible vertical elements
    """
    verticalSet = []
    i = 0
    while i < lawndim[1]:
        verrow = []
        j = 0
        while j < lawndim[0]:
            verrow.append(lawn[j][i])
            j += 1
        verticalSet.append(verrow)
        i += 1
    return verticalSet


def findMinH(lawndim, lawn):
    maxc = 0
    for lawnRow in lawn:
        if maxc  > max(lawnRow) and maxc  > 0:
            maxc  = max(lawnRow)
    return maxc

# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1: return
#         yield start
#         start += len(sub)

def lawnmover(lawndim, lawn):
    import re

    horiset = horizontal(lawndim,lawn)
    veriset = vertical(lawndim, lawn)

    completeLawn = []
    completeLawn.append(horiset)
    completeLawn.append(veriset)

    i = 0
    # print(lawndim)
    # print completeLawn
    while i < lawndim[0]:
        # print(">>" + str(lawn[i]))
        maxc = max(lawn[i])
        minc = min(lawn[i])
        if maxc == minc:
            i += 1
            pass
        else:
            ace = [m.start() for m in re.finditer(str(minc), ''.join(str(x) for x in lawn[i]))]
            for j in ace:
                if  max(completeLawn[1][j]) == min(completeLawn[1][j]):
                    pass
                else:
                    return "NO"
            i += 1
    return "YES"


def main(inFile, outfile):
    """
    file read write function
    """
    cases = int(inFile.readline())
    cases += 1
    i = 1
    while i < cases:
        lawn = []
        lawnDim = (map(lambda x : int(x), inFile.readline().split("\n")[0].split()))
        j = 0
        while j < lawnDim[0]:
            lawn.append(map(lambda x : int(x), inFile.readline().split("\n")[0].split()))
            j += 1
        casecounter = lawnmover(lawnDim, lawn)
        outWrite = "Case #%d: %s\n" % (i, casecounter)
        outFile.write(outWrite)
        i += 1
    outFile.close()
    inFile.close()

if __name__ == "__main__":
    inFile = open("B.in", "r")
    outFile = open("B.out", "w")
    main(inFile, outFile)