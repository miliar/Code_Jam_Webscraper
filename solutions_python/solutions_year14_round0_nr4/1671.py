import sys

infilename = sys.argv[1]
infile = open(infilename)
outfile = open("out","w")
numtry = int(infile.readline())
for ctry in range(0, numtry):
    numblocks = int(infile.readline())
    Naomiblocks = map(float, infile.readline().split(' '))
    Naomiblocks.sort()
    Kenblocks = map(float, infile.readline().split(' '))
    Kenblocks.sort()
    #print Naomiblocks, Kenblocks
    DW = 0
    W = 0
    NB = Naomiblocks[:]
    KB = Kenblocks[:]
    while True:
        if not NB:
            break
        if NB[0] > KB[-1]:
            DW += len(NB)
            break
        if NB[-1] < KB[0]:
            break
        if NB[0] < KB[0]:
            del NB[0]
            del KB[-1]
        else:
            del NB[0]
            del KB[0]
            DW += 1
    
    NB = Naomiblocks[:]
    KB = Kenblocks[:]
    while True:
        if not NB:
            break
        if NB[0] > KB[-1]:
            W += len(NB)
            break
        if NB[-1] < KB[0]:
            break
        for pos in range(len(NB)):
            if KB[pos] > NB[0]:
                del KB[pos]
                del NB[0]
                break
    textout = "Case #%d: %d %d" % (ctry +1, DW, W)
    print textout
    outfile.write(textout + "\n")
    
outfile.close()
infile.close()
