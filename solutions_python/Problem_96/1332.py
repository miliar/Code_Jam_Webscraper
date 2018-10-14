import sys
infile = sys.argv[1]

f = open(infile,'r')
cases = int(f.readline())
for case in range(cases):
    line = f.readline()
    split = line.strip().split(' ')
    s = int(split[1])
    p = int(split[2])
    scores = split[3:]

    pmax = 0
    for score in scores:
        score = int(score)
        if 3*p - 2 <= score and p <= score:
            pmax += 1
        elif 3*p-4 <= score and s > 0 and p <= score:
            s -= 1
            pmax += 1
    print 'Case #%s: %s' % (case+1, pmax)

