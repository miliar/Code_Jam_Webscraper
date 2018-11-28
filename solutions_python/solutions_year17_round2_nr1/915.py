INFILENAME = 'A-large.in'
OUTFILENAME = 'output.out'

with open(INFILENAME) as infile, open(OUTFILENAME, 'w') as outfile:
    testcase = int(infile.readline())
    for i in range(testcase):
        dist, nhorses = map(int, infile.readline().split())
        maxtime = 0
        for _ in range(nhorses):
            pos, mxspeed = map(int, infile.readline().split())
            time = (dist - pos) / mxspeed
            if maxtime < time:
                maxtime = time
        outfile.write('Case #{0}: {1}\n'.format(i + 1, dist/maxtime))
