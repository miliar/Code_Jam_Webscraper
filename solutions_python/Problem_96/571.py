def makeScores(s):
    scores = []
    c = int(s / 3)
    c1 = c - 3
    if c1 < 0:
        c1 = 0
    for i1 in range(c1, c + 3):
        for i2 in range(c1, c + 3):
            for i3 in range(c1, c + 3):
                if i1 + i2 + i3 == s:
                    ss = [i1, i2, i3]
                    ss.sort()
                    if ss[0] + 2 >= ss[2]:
                        try:
                            scores.index(ss)
                        except:
                            scores.append(ss)
    return scores

def isStrange(s):
    if s[0] + 2 == s[2]:
        return True
    return False

def isGood(s, p):
    if s[0] >= p or s[1] >= p or s[2] >= p:
        return True
    return False

def hasGoodNotStrange(ss, p):
    for i in range(0, len(ss)):
        if not isStrange(ss[i]):
            if isGood(ss[i], p):
                return True
    return False

def hasGoodStrange(ss, p):
    for i in range(0, len(ss)):
        if isStrange(ss[i]):
            if isGood(ss[i], p):
                return True
    return False

def __main__():
    f = open("B-large.in", "rt")
    T = int(f.readline())
    
    fout = open("B.out", "wt+")
    
    for t in range(0, T):
        ss = f.readline().strip("\n").split()
        N = int(ss[0])
        S = int(ss[1])
        p = int(ss[2])
        K = 3
        
        totals = []
        for i in range(0, N):
            totals.append(int(ss[K + i]))
        
        mustStrange = 0
        
        scores = []
        for i in range(0, N):
            s = makeScores(totals[i])
            if len(s) == 1:
                if s[0][0] + 2 == s[0][2]:
                    mustStrange += 1
            scores.append(s)
        
        potentialStrange = S - mustStrange
        
        print(scores)
        
        R = 0
        for i in range(0, N):
            if hasGoodNotStrange(scores[i], p):
                R += 1
                continue
            
            if potentialStrange > 0:
                if hasGoodStrange(scores[i], p):
                    R += 1
                    potentialStrange -= 1
        
        print(R)
        
        fout.write("Case #%(case)s: %(result)s\n" % {"case": t + 1, "result": R})
        

if __name__ == "__main__":
    __main__()