__author__ = 'ligenjian'

inputfile = open('data/A-small-attempt0.in.txt')
outputfile = open('output/A.txt', 'w')

t = int(inputfile.readline())

for i in range(t):
    firstguess = int(inputfile.readline())
    for j in range(4):
        if j == firstguess - 1:
            firstlist = map(int, inputfile.readline().split(' '))
        else:
            inputfile.readline()
    secondguess = int(inputfile.readline())
    for j in range(4):
        if j == secondguess - 1:
            secondlist = map(int, inputfile.readline().split(' '))
        else:
            inputfile.readline()
    matchcount = 0
    for num in firstlist:
        if num in secondlist:
            matchnum = num
            matchcount += 1
    if matchcount == 1:
        print>>outputfile, 'Case #%d: %d' % ( i + 1, matchnum)
    elif matchcount == 0:
        print>>outputfile, 'Case #%d: Volunteer cheated!' % (i + 1)
    else:
        print>>outputfile, 'Case #%d: Bad magician!' % (i + 1)
