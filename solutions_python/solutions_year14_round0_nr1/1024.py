filename = 'A-small-attempt0'
inputfile = filename + '.in'
outputfile = filename + '.out'

with open(inputfile) as input, open(outputfile, 'w') as output:
    T = int(input.readline())
    for t in xrange(T):
        a1 = int(input.readline())
        r1 = None
        for i in xrange(4):
            row = map(int, input.readline().split())
            if i + 1 == a1:
                r1 = set(row)

        a2 = int(input.readline())
        r2 = None
        for i in xrange(4):
            row = map(int, input.readline().split())
            if i + 1 == a2:
                r2 = set(row)

        r = r1 & r2
        if len(r) == 0:
            output.write("Case #{t}: Volunteer cheated!\n".format(t=t+1))
        elif len(r) == 1:
            output.write("Case #{t}: {r}\n".format(t=t+1, r=iter(r).next()))
        else:
            output.write("Case #{t}: Bad magician!\n".format(t=t+1))