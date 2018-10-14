import sys, math

def map(func, l):
    return [func(i) for i in l]

def parseCase(instrm):
    return instrm.readline().strip().split(" ")[1]

def solveCase(case):
    res = 0
    standing = 0
    for pos in range(len(case)):
        d = int(case[pos])
        if pos > standing:
            toInvite = pos - standing
            standing += toInvite
            res += toInvite
        standing += d
    return res
    

if __name__=="__main__":
    instrm = open(sys.argv[1])
    cases = int(instrm.readline().strip())
    for c in range(cases):
        input = parseCase(instrm)
        res = str(solveCase(input))
        print("Case #" + str(c+1) +": "+res)
    instrm.close()
