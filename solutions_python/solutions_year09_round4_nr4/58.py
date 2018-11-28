import psyco
psyco.full()

#1. output format
sepInOutput = " "

#2. read problem setup
def readProblemSetup(fi):
    # read problem parameters
    result = map(int, fi.readline().split())
    # read other things

    # return as a tuple
    return result

#3. read problem case
def readCase(fi):
    # read one case
    N = int(fi.readline())
    return [map(int, fi.readline().split()) for _ in range(N)]

#4. solve case
def interact(c1, c2, r):
    dx = c1[0] - c2[0]
    dy = c1[1] - c2[1]
    d = r+r-c1[2]-c2[2]
    return dx*dx+dy*dy <= d*d

def interactall(c1, c2s, r):
    for c2 in c2s:
        if not interact(c1, c2, r):
            return False
    return True

def checkCircle(c, classes, r):
    c1s, c2s = classes
    result = []
    if interactall(c, c1s, r):
        result.append((c1s+[c], c2s))
    if interactall(c, c2s, r):
        result.append((c1s, c2s+[c]))
    return result

def test(cs, classes, r):
    # check if any of c in cs can be in at least one class
    if not cs:
        return True
    newclasses = checkCircle(cs[0], classes, r)
    if not newclasses:
        return False
    for newclasses in newclasses:
        if test(cs[1:], newclasses, r):
            return True
    return False
    
def solveCase(case, setup):
    # solve the case
    rguess_min = max(c[2] for c in case)
    rguess_max = 900
    class1 = [case[0]]
    class2 = []
    case.pop(0)
    while rguess_max - rguess_min > 0.0000001:
        rguess_mid = (rguess_min + rguess_max)/2.0
        if test(case, (class1, class2), rguess_mid):
            rguess_max = rguess_mid
        else:
            rguess_min = rguess_mid
    return rguess_max

#5. format solution to string
def solution2str(solution):
    return "%.7f" % solution

def solveFile(f, f2):
    fi = open(f, 'r')
    if f2 == None:
        fo = sys.stdout
    else:
        fo = open(f2, 'w')
    # 1. read problem setup if needed
    setup = readProblemSetup(fi)

    N = setup[0]
    # 2. solve the cases
    for i in range(1, N+1):
        fo.write("Case #%d:%s%s\n" % (i, sepInOutput,
                                    solution2str(solveCase(readCase(fi), setup))))
if __name__=='__main__':
    import sys
    if len(sys.argv) == 2:
        solveFile(sys.argv[1], sys.argv[1]+".out")
    elif len(sys.argv) == 3:
        solveFile(sys.argv[1], None)
    else:
        # run tests
        print "running tests:"
        
