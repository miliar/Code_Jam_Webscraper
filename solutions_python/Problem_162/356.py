import sys, os, math
inpath = sys.argv[1]

def invertDigits(n):
    cs = str(n)
    newcs = ""
    startup = True
    for c in reversed(cs):
        if startup and (c == '0'):
            continue
        newcs += c
        startup = False
    return int(newcs)

def preSolve(N):
    times = [0]*(N+1)
    times[1] = 1
    solved = [1]
    time = 2
    remaining = N-1
    while remaining > 0 and len(solved) > 0:
        newsolved = []
        for sol in solved:
            tsol = times[sol] #you can get to sol in tsol time
            #try to increase sol
            if sol+1 <= N and times[sol+1]==0:
                times[sol+1] = time
                newsolved.append(sol+1)
                remaining -= 1
            #try to inver the digits
            isol = invertDigits(sol)
            if isol <= N and times[isol]==0:
                times[isol] = time
                newsolved.append(isol)
                remaining -= 1
        solved = newsolved
        time += 1
    return times

times = preSolve(1000000)


def parseCase(instrm):
    return int(instrm.readline().strip())


def solveCase(case):
    return times[case]

def solveCase2(num):
    if times[num] != 0:
        return times[num]
    guess = solveCase(num-1)
    inum = invertDigits(num)
    if len(str(num)) == len(str(inum)) and inum < num:
        guess2 = solveCase(inum)
        if guess2 < guess:
            guess = guess2
    return 1 + guess


if __name__=="__main__":
    instrm = open(inpath, 'r')
    cases = int(instrm.readline().strip())
    for i in range(cases):
        case = parseCase(instrm)
        res = solveCase(case)
        print("Case #" + str(i+1) + ": " + str(res))
    instrm.close()


