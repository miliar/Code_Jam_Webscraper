from re import match
words = []
outFile = open("out.out", "w")
case = 1
for ind, line in enumerate(open("A-large.in","U")):
    if ind == 0:
        toks = line.split()
        L = int(toks[0])
        D = int(toks[1])
        N = int(toks[2])
    if 1 <= ind <= D:
        words.append(line.strip())
    if D < ind:
        pattern = line.strip()
        pattern = pattern.replace("(","[")
        pattern = pattern.replace(")","]")
        numMatched = 0
        for word in words:
            if match(pattern, word) is not None:
                numMatched += 1
        output = "Case #%d: %d\n" % (case, numMatched)
        # print output
        outFile.write(output)
        case += 1
outFile.close()
