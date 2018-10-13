def isnondecreasing(lis):
    topseen = 0
    for d in lis:
        if d < topseen:
            return False
        topseen = max(topseen, d)
    return True


def nondecreasingSubSequence(lis):
    i = 0
    topseen = 0
    for d in lis:
        if d < topseen:
            break
        topseen = max(topseen, d)
        i += 1
    return i


def digstoint(numList):
    return int(''.join(map(str, numList)))


def inttodigs(num):
    return [int(d) for d in str(num)]


def solve(representation):
    num = representation
    # print(num)
    digs = [int(d) for d in str(num)]
    if isnondecreasing(digs): return num

    print(digs)
    maxlen = nondecreasingSubSequence(digs)
    # print(digs[:maxlen])
    while maxlen > 0:
        newdigs = inttodigs(digstoint(digs[:maxlen]) - 1)
        if isnondecreasing(newdigs):
            return digstoint(newdigs + [9] * (len(digs) - maxlen))
        maxlen -= 1
    return [9] * (len(digs) - 1)


def getprob(content):
    prob = content[0]
    del content[0]
    return prob


def parseprob(text):
    return int(text)


def readAndSolve():
    d = "C:\\Users\\dave\\Downloads\\"
    infile = "B-large.in"
    content = []
    with open(d + infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    numprobs = int(content[0])
    del content[0]

    lines = []
    for pnum in range(numprobs):
        prob = getprob(content)
        representation = parseprob(prob)
        solved = solve(representation)
        str = 'Case #{}: {}'.format(pnum + 1, solved)
        print(str)
        lines.append(str)

    outfname = infile.replace(".in", ".out")
    outfile = "C:\\Users\\dave\\PycharmProjects\\codejam_2017_qualifier\\" + outfname
    f = open(outfile, 'w')
    print('\n'.join(lines), file=f)
    f.close()


readAndSolve()
