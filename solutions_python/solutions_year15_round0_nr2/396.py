import sys, math

def map(func, l):
    return [func(i) for i in l]

def parseCase(instrm):
    instrm.readline()
    return map(int, instrm.readline().strip().split(" "))

def solveCase(case):
    m = max(case)
    score = m
    for sec in range(1,m):
        #split so that every diner ends in sec minutes
        splits = 0
        for c in case:
            splits += math.ceil(c/sec) - 1
        totmin = splits + sec
        if totmin < score:
            score = totmin
    return score

if __name__=="__main__":
    instrm = open(sys.argv[1])
    cases = int(instrm.readline().strip())
    for c in range(cases):
        input = parseCase(instrm)
        res = str(solveCase(input))
        print("Case #" + str(c+1) +": "+res)
    instrm.close()
