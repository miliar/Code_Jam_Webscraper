import sys

def handle(infile, outfile):
    t = int(infile.readline())
    nab, nba = [int(x) for x in infile.readline().split()]
    
    global times, matches
    times = [None] * nab, [None] * nba
    matches = [-1] * nab, [-1] * nba
    
    for i in range(nab):
        trip = infile.readline().split()
        times[0][i] = [reduce(lambda h, m: m + h * 60, [int(n) for n in time.split(':')]) for time in trip]
        
    for i in range(nba):
        trip = infile.readline().split()
        times[1][i] = [reduce(lambda h, m: m + h * 60, [int(n) for n in time.split(':')]) for time in trip]
        
    match(0, 1, t)
    match(1, 0, t)
    
    tab = matches[0].count(-1)
    tba = matches[1].count(-1)
    outfile.write(' %d %d' % (tab, tba))
    
def match(a, b, t):
    for i in range(len(times[a])):
        mintime = 10000
        minindex = -1
        for j in range(len(times[b])):
            time = times[b][j][0] - times[a][i][1] - t
            if time >= 0 and mintime > time and matches[b][j] == -1:
                if minindex != -1: matches[b][minindex] = -1
                matches[b][j] = i
                
                mintime = time
                minindex = j

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1], 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
    print 'Case #%d' % (i + 1)
    outfile.write('Case #%d:' % (i + 1))
    result = handle(infile, outfile)
    outfile.write('\n')
