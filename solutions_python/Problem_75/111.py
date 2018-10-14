import sys;

def line():
    return sys.stdin.readline()

def strs():
    return line().split()

def array(func):
    return map(func, strs())

def readall():
    global inputIter
    inputIter = iter(sys.stdin.read().split())

def nxt(func = None):
    if func:
        return func(next(inputIter))
    else:
        return next(inputIter)

if __name__ == '__main__':
    readall()
    for case in range(1,nxt(int)+1):
        combine = {}
        for i in range(nxt(int)):
            s = nxt()
            combine[(s[0],s[1])] = combine[(s[1],s[0])] = s[2]
    
        opposed = {}
        for i in range(nxt(int)):
            s = nxt()
            opposed[(s[0],s[1])] = opposed[(s[1],s[0])] = 1
    
        _ = nxt()
        s = nxt()
        r = []
        for c in s:
            if r:
                key = (r[-1], c)
                if key in combine:
                    r[-1] = combine[key]
                    continue
    
            for rc in r:
                key = (rc, c)
                if key in opposed:
                    r = []
                    break
            else:
                r.append(c)

        print("Case #%d: %s" % (case, str(r).replace("'","")))
