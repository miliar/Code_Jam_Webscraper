# Guillermo Ortas

# dataFile = open("Q_A.txt", 'r')
# dataFile = open("A-small-attempt0.in", 'r')
dataFile = open("A-large.in", 'r')

target = open("output.out", 'w+')

rows = str(dataFile.readline())

def flip(k, i, pancake_row, flips):
    row = list(pancake_row)
    if k <= len(pancake_row) - i:
        j = 0
        while j < k:
            if row[i+j] == "-":
                row[i+j] = "+"
            else:
                row[i+j] = "-"
            j += 1
        flips += 1
    else:
        return "IMPOSSIBLE", -1
    return "".join(row), flips

m = 1
for line in dataFile:
    pancake_row = str(line.split(" ")[0])
    k = int(line.split(" ")[1])
    # print pancake_row
    # print k
    flips = 0
    for i in range(len(pancake_row)):
        if pancake_row[i] == "-":
            pancake_row, flips = flip(k, i, pancake_row, flips)
    if flips >= 0:
        target.write("Case #" + str(m) + ": " + str(flips))
    else:
        target.write("Case #" + str(m) + ": " + "IMPOSSIBLE")
    target.write("\n")
    m += 1

target.close()