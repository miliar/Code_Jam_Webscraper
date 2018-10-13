import sys

inName = sys.argv[1]
outName = inName[:inName.index('.')] + '.out'

fin = open(inName)
fout = open(outName, 'w')

cases = int(fin.readline())

def pp(case, out):
    ss= "Case #%d: %s\n" % (case+1, out)
    print ss,
    fout.write(ss)

for case in xrange(cases):
    line = fin.readline().strip().split(' ')
    sMax = line[0]
    ks = map(int, list(line[1]))
    #print sMax, ks

    friends = 0
    numStanding = 0
    for shyness, numPeople in enumerate(ks):
        newPeople = max(shyness - numStanding, 0)
        friends += newPeople
        numStanding += newPeople
        numStanding += numPeople

    #print friends
    pp(case, friends)

fout.close()
