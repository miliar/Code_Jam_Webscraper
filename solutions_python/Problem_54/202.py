def gcd(a, b):
    """ euclid's gcd """
    while b != 0:
        (a, b) = (b, a%b)
    return a

def solve(filecontent):
    lines = filecontent.splitlines()
    C = int(lines[0])
    out = []
    for tcase in xrange(1,C+1):
        line = lines[tcase].split(" ")
        N = int(line[0])
        t = map(int,line[1:])
        tcaseOut = ("Case #%d: " % (tcase,))

        # we find the min
        tmin = min(t)
        # subtract tmin from each t
        tsub = [x-tmin for x in t]
        # discard 0 that was derived from tmin
        tsub = [x for x in tsub if x != 0]
        # perform gcd on all these numbers
        T = reduce(gcd, tsub)

        tcaseAnswer = (T - (tmin % T)) % T
        tcaseOut += "%d" % (tcaseAnswer)
        out.append(tcaseOut)
    return "\n".join(out)

f = file("codejam/B-large.in").read()
file("codejam/B-large.out",'w').write(solve(f))
