# Password Problem

i = open("A-small-attempt0.in", "r")
o = open("A-small.out", "w")

_cases = [['C', 'X'], ['CC', 'CX', 'XC', 'XX'], ['CCC', 'CCX', 'CXC', 'CXX', 'XCC', 'XCX', 'XXC', 'XXX']]

T = int(i.readline())

for c in range(1, T + 1):
    A, B = map(int, i.readline().replace('\n','').split(' '))
    PA = map(float, i.readline().replace('\n','').split(' '))

    ekeystrokes = []
    bXkeystrokes = []
    ckeystrokes = []
    cases = _cases[A - 1]

    for case in cases:
        cprob = 1
        for x in range(len(case)):
            if 'C' == case[x]:
                cprob *= PA[x]
            else:
                cprob *= 1 - PA[x]

        ekeystrokes.append(cprob * (B + 2))

        bkeystrokes = []
        for y in range(1, A + 1):
            rem = case[:-y]
            if rem.count('X') > 0:
                bkeystrokes.append(cprob * (2*y + 2*B - A + 2))
            else:
                bkeystrokes.append(cprob * (2*y + B - A + 1))
        bXkeystrokes.append(bkeystrokes)

        if case.count('X') > 0:
            ckeystrokes.append(cprob * (2*B - A + 2))
        else:
            ckeystrokes.append(cprob *(B - A + 1))
    
    keystrokes = []
    keystrokes.append(sum(ekeystrokes))
    keystrokes.append(sum(ckeystrokes))
    
    for z in range(A):
        bsum = 0
        for bXkeystroke in bXkeystrokes:
            bsum += bXkeystroke[z]
        keystrokes.append(bsum)

    result = "%.6f" % min(keystrokes)
    o.write("Case #{0}: {1}\n".format(c, result))

i.close()
o.close()