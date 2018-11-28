import re


def flip(pancakes, spatula, i):
    for j in range(i, i + spatula):
        pancakes[j] = 1 - pancakes[j]


def solve(representation):
    pancakes, spatula = representation
    # print(pancakes, spatula)

    flips = 0
    for i in range(len(pancakes) - spatula + 1):
        if pancakes[i] == 0:
            flip(pancakes, spatula, i)
            flips += 1
    if not all(p == 1 for p in pancakes): return 'IMPOSSIBLE'
    return str(flips)


def getprob(content):
    prob = content[0]
    del content[0]
    return prob


def parseprob(text):
    match = re.match("([+-]+) (\d+)", text)
    if not match:
        print('regular expression is fucked up')
        exit(1)
    pancakes = [0 if p == '-' else 1 for p in match.group(1)]
    spatula = int(match.group(2))
    return pancakes, spatula


def readAndSolve():
    d = "C:\\Users\\dave\\Downloads\\"
    infile = "A-large.in"
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
