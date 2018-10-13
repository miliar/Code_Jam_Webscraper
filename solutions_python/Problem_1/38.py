import sys

def getline():
    return sys.stdin.readline()

cases = int(getline())

for case in range(cases):

    # read engine names
    S = int(getline())
    engines = {}
    for eng in range(S):
        name = getline()
        engines[name] = eng

    # read queries
    Q = int(getline())
    swi = [0]*S

    for que in range(Q):
        eng = engines[getline()]
        # eng = no. of the current engine
        sw2 = swi[:]
        sw2[eng:eng+1] = []
        mi = min(sw2)
        swi[eng] = mi + 1

    mini = min(swi)
    print "Case #%d: %d" % (case+1, mini)
