def solveNums(a, b):
    p = set()
    num = 0
    for i in xrange(a,b+1):
        num += testNum(i, a, b, p)
    return num

def testNum(i, a, b, p):
    num = 0
    s = str(i)
    for brk in xrange(0, len(str(i))-1):
        cand = s[brk+1:] + s[:brk+1]
        if a <= int(cand) <= b and int(cand) > i:
            strRep = s + cand
            if strRep not in p:
                num += 1
                p.add(strRep)
    return num

def solve(fil):
    fout = open("out.txt", mode = "wb")
    lNum = 0
    with open(fil) as f:
        for line in f:
            if lNum > 0:
                (a,b) = [int(i) for i in line.split(" ")]
                fout.write("Case #%d: %d\r\n" % (lNum, solveNums(a, b)))
            lNum += 1
    fout.close()
