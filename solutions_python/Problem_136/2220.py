inf = open(input('Input File: '))
ouf = open(input('Output File: '), 'w')

test_cases = int(inf.readline())


for i in range(1, test_cases + 1):
    C, F, X = list(map(lambda x: float(x), str.split(inf.readline(), ' ')))
    R = 2.0
    FRM = 0.0
    lreq = lambda : X/R + FRM
    lnreq = lambda :(X/(R + F)) + FRM + C/R

    nreq = lnreq()
    req = lreq()

    while req > nreq:
        FRM += (C / R)
        R += F
        nreq = lnreq()
        req = lreq()

    ouf.write('Case #%d: %f\n' % (i, req))
