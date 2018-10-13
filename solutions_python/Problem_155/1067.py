import sys
# parse command line
if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = open('a.in')


T = int(inf.readline())

for x in range(1,T+1):
    line = inf.readline().split(' ')
    smax = int(line[0])

    s = map(lambda n: int(n), line[1].strip())

    standing = 0
    y = 0
    for i in range(smax+1):
        if standing < i:
            diff = i - standing
            y += diff
            standing += diff
        standing += s[i]


    print 'Case #%d: %d' % (x, y)