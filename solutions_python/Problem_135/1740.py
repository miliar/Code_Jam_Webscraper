import sys
try:
    fname = sys.argv[1]
except:
    print("input filename")
    sys.exit(1)
infile = open(fname)
outfile = open("out","w")
numtry = int(infile.readline())
for ctry in range(0, numtry):
    firstrownum = int(infile.readline())
    first = []
    for row in range(0,4):
        first.append(infile.readline().strip())
    firstset = set(first[firstrownum-1].split(' '))
    secondrownum = int(infile.readline())
    second = []
    for row in range(0,4):
        second.append(infile.readline().strip())
    secondset = set(second[secondrownum-1].split(' '))
    print(firstrownum, first, firstset, secondrownum, second, secondset,
          firstset & secondset, sep = '\n')
    textout = "Case #%d: " % (ctry+1)
    result = firstset & secondset
    if not(result):
        textout += "Volunteer cheated!"
    if len(result) == 1:
        textout += str(list(result)[0])
    if len(result) > 1:
        textout += "Bad magician!"
    print(textout)
    outfile.write(textout+'\n')
outfile.close()    
infile.close()
