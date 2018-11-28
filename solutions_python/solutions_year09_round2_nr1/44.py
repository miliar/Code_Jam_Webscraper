
def parse(t, i=0):
    T = []
    w = f = ""
    while i < len(t):
        if t[i] == "(":
            sub, i = parse(t, i+1)
            T.append(sub)
        elif t[i].isspace() or t[i] == ")":
            if w:
                T.append(float(w))
                w = ""
            if f:
                T.append(f)
                f = ""
            if t[i] == ")":
                return T, i
        elif t[i].isalpha():
            f += t[i]
        else:
            w += t[i]
        i += 1
    return T[0]

def howCute(T, flist, p=1.0):
    p *= T[0]
    if len(T) == 1:
        return p
    if T[1] in flist:
        return howCute(T[2], flist, p)
    else:
        return howCute(T[3], flist, p)

def DecisionTree():
    t = ""
    L = int(raw_input())
    for i in xrange(L):
        t += raw_input()
        t += " "
    T = parse(t)
    A = int(raw_input())
    for i in xrange(A):
        flist = raw_input().split()[2:]
        print "%.7f" % howCute(T, flist)

#---------------------------------------------------------------

N = int(raw_input())
for testcase in range(N):
    print "Case #%d:" % (testcase+1)
    DecisionTree()
