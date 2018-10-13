inpath = "A-large.in"
outpath = "A-large.out"

infile = open(inpath, "r")

line = infile.readline().rstrip()
L, D, N = [int(s) for s in line.split(" ")]

words = [infile.readline().rstrip() for x in range(D)]

cases = []
for x in range(N):
    rawcase = infile.readline().rstrip()
    tokens = []
    for t in range(L):
        char = rawcase[0]
        if char == "(":
            endindex = rawcase.index(")")
            tokens.append(rawcase[1:endindex])
            rawcase = rawcase[endindex + 1:]
        else:
            tokens.append(char)
            rawcase = rawcase[1:]
    cases.append(tokens)

infile.close()

matches = {}

for word in words:
    for i in range(len(cases)):
        case = cases[i]
        match = True
        for letter, token in zip(word, case):
            if letter not in token:
                match = False
                break
        if match:
            matches[i] = matches.get(i, 0) + 1

outfile = open(outpath, "w")

for i in range(len(cases)):
    outfile.write("Case #%d: %d\n" % (i + 1, matches.get(i, 0)))

outfile.close()