def getLength10(x):
    if x < 10:
        return 1
    if x < 100:
        return 2
    if x < 1000:
        return 3
    if x < 10000:
        return 4
    if x < 100000:
        return 5
    if x < 1000000:
        return 6
    if x < 10000000:
        return 7
    if x < 100000000:
        return 8
    return 9

def makeRecycled(x, l):
    L = getLength10(x)
    D = pow(10, l)
    M = pow(10, L - l)
    return int(x / D) + (x % D) * M

def __main__():
    f = open("C-small-attempt0.in", "rt")
    T = int(f.readline())
    
    fout = open("C.out", "wt+")
    
    for t in range(0, T):
        ss = f.readline().strip("\n").split()
        A = int(ss[0])
        B = int(ss[1])
        
        pairs = set()
        
        R = 0
        for x in range(A, B + 1):
            for l in range(1, getLength10(x)):
                xr = makeRecycled(x, l)
                if x < xr and xr >= A and xr <= B:
                    p = (x, xr)
                    pairs.add(p)
        R = len(pairs)
        
        fout.write("Case #%(case)s: %(result)s\n" % {"case": t + 1, "result": R})

if __name__ == "__main__":
    __main__()