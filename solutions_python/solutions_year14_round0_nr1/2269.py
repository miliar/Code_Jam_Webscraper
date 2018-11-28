import os

infilename = "A-small-attempt0.in"
in_file = open(infilename)

numcases = int(in_file.readline())
totalout = ""

for casenum in range(numcases):
    rowNum = int(in_file.readline())
    row = None
    for i in range(4):
        tmpRow = [int(w) for w in in_file.readline().split()]
        if i + 1 == rowNum:
            row = tmpRow

    rowNum = int(in_file.readline())
    row2 = None

    for i in range(4):
        tmpRow = [int(w) for w in in_file.readline().split()]
        if i + 1 == rowNum:
            row2 = tmpRow

    result = None
    for num in row:
        if num in row2:
            if result == None:
                result = num
            else:
                result = "Bad magician!"

    if result == None:
        result = "Volunteer cheated!"

    outstr = "Case #" + str(casenum + 1) + ": " + str(result)
    totalout += outstr + "\n"
    print(outstr)

writetofile = False
if "small" in infilename:
    outprefix = "small"
    writetofile = True
elif "large" in infilename:
    outprefix = "large"
    writetofile = True
#writetofile = False

if writetofile:
    filenum = 0
    while True:
        outfilename = outprefix + str(filenum) + ".out"
        filenum += 1
        if not os.path.isfile(outfilename):
            break
    out_file = open(outfilename, 'w+')
    out_file.write(totalout)
    out_file.close()

in_file.close()
