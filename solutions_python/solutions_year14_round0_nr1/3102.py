import sys


def solution(inFile):
    r = []
    N = inFile.readline()
    for i in range(4):
        if i == int(N) - 1:
            row1 = inFile.readline()
            continue
        inFile.readline()
    N = inFile.readline()
    for i in range(4):
        if i == int(N) - 1:
            row2 = inFile.readline()
            continue
        inFile.readline()
    row1 = row1.split(" ")
    row2 = row2.split(" ")
    for elem1 in row1:
        for elem2 in row2:
            if elem1.rstrip() == elem2.rstrip():
                r.append(elem1)
    if len(r) == 1:
        return "".join(r)
    if len(r) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

inFile = open(sys.argv[1], "r")
outFile = open("out", "w")

N = int(inFile.readline())
for i in range(N):
    outFile.write("Case #%d: " % (i + 1))
    outFile.write(solution(inFile))
    outFile.write("\n")

inFile.close()
outFile.close()