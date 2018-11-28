def solveCase(s, p, scores):
##    print s, p, scores
    good = 0
    needSurprise = 0
    for scr in scores:
        if scr == 3*p-4 and p-2 >= 0 and p <= 10:
            needSurprise += 1
        elif scr == 3*p-3 and p-2 >= 0 and p <= 10:
            needSurprise += 1
        elif scr >= 3*p-2 and int(scr/3) >= 0:
            good += 1
    return good + min(needSurprise, s)

def parseSolveCase(s):
    l = parseCase(s)
    return solveCase(l[1], l[2], l[3:])

def parseCase(s):
    return [int(i) for i in s.split(" ")]

def solve(fil):
    fout = open("out.txt", mode = "wb")
    lNum = 0
    with open(fil) as f:
        for line in f:
            if lNum > 0:
                fout.write("Case #%d: %s\r\n" \
                           % (lNum, parseSolveCase(line)))
            lNum += 1
    fout.close()
