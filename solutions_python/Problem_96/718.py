t = open('input2.txt')
t.readline()

SUR = {}
NOTSUR = {}

for index, l in enumerate(t):
    l = map(int, l.split())
    N = l[0]
    S = l[1]
    p = l[2]
    T = l[3:]
    smallest = max(p-2, 0) * 2 + p
    cbs = 0
    good = 0
    for t in T:
        if t < smallest:
            continue
        elif t in (3*p - 4, 3*p - 3):
            cbs += 1
        else:
            good += 1
    print "Case #%d: %d" % (index+1, good + min(S, cbs))
