import sys, math

def map(func, l):
    return [func(i) for i in l]

strToNum = {"i":2, "j":3, "k":4}

rules = [ 
    [1, 2, 3, 4],
    [2,-1, 4,-3],
    [3,-4,-1, 2],
    [4, 3,-2,-1]] 

def sign(q):
    if q < 0:
        return -1
    if q > 0:
        return 1
    raise Exception
    return 0

def prod(q1, q2):
    s = sign(q1)*sign(q2)
    return s*(rules[abs(q1)-1][abs(q2)-1])


def parseCase(instrm):
    X = int(instrm.readline().strip().split(" ")[1])
    s = [strToNum[i] for i in instrm.readline().strip()]
    return s*X

def makeDP():
    return [0]*3

def solveCase(case):
    dp = makeDP()
    dp[0] = 1
    for c in case:
        newdp = makeDP()
        for nsegm in range(3):
            if dp[nsegm] == 0:
                continue
            ff = prod(dp[nsegm], c)
            newdp[nsegm] = ff
        for nsegm in range(2):
            if abs(newdp[nsegm])==(nsegm+2):
                if (newdp[nsegm+1] != 0) and (newdp[nsegm+1] != sign(newdp[nsegm])):
                    raise Exception("something went wrong")
                newdp[nsegm+1] = sign(newdp[nsegm])
        #print("dp:")
        #print(dp)
        #print("new dp:")
        #print(newdp)
        
        dp = newdp
        
    if dp[2]==4:
        return "YES"
    return "NO"

if __name__=="__main__":
    instrm = open(sys.argv[1])
    cases = int(instrm.readline().strip())
    for c in range(cases):
        input = parseCase(instrm)
        res = str(solveCase(input))
        print("Case #" + str(c+1) +": "+res)
    instrm.close()
