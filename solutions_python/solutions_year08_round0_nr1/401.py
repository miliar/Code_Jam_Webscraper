fin = open("input.txt", "r")
fout = open("output.txt", "w")
casesCount = int(fin.readline())
for curCase in range(1, casesCount + 1):
    enginesCount = int(fin.readline())
    enginesList = [''] * enginesCount
    for i in range(enginesCount):
        enginesList[i] = fin.readline().strip()
    queryCount = int(fin.readline())
    enginesLeft = [x for x in enginesList]
    result = 0
    for i in range(queryCount):
        query = fin.readline().strip()
        if query in enginesLeft:
            if len(enginesLeft) == 1:
                result += 1
                enginesLeft = [x for x in enginesList]
            del enginesLeft[enginesLeft.index(query)]
    fout.write("Case #%i: %i\n" % (curCase, result))

fin.close()
fout.close()