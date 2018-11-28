infile = open('A-large.in.txt')
outfile = open('A-large.out', 'w')

lines = infile.read().split('\n')
casecount = int(lines.pop(0))

for casenum in range(1, casecount+1):
    shynessstring = lines.pop(0).split()[1]
    audienceshyness = map(int, list(shynessstring))
    neededfriends = 0
    standing = 0
    for i in range(len(audienceshyness)):
        if standing<i:
            neededfriends += i - standing
            standing += i - standing
        standing += audienceshyness[i]
    print >> outfile, "Case #%i: %i"%(casenum, neededfriends)