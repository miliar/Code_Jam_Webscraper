f = open("magicka.large.in", "r")

t = int(f.readline())

C = []
D = []
N = []

COMB = []
HATE = []
LIST = []

l = 0

for line in f:
    v = line.split(" ")
    
    c = int(v[0])

    C.append(c)
    COMB.append([])
    for i in range(0, c):
        COMB[l].append(v[1+i])

    d = int(v[1+c])
    D.append(d)
    HATE.append([])
    for i in range(0, d):
        HATE[l].append(v[1+c+1+i])

    n = int(v[1+c+1+d])
    N.append(n)
    LIST.append(v[1+c+1+d+1])

    l += 1

f.close()



def combine(R, item, u):
    last = R[len(R)-1]

    for i in range(0, C[u]):
        if (item == COMB[u][i][0] and last == COMB[u][i][1]) or (item == COMB[u][i][1] and last == COMB[u][i][0]):
            R[len(R)-1] = COMB[u][i][2]
            return True

    return False

def opposes(item1, item2, u):
    for i in range(0, D[u]):
        if (item1 == HATE[u][i][0] and item2 == HATE[u][i][1]) or (item1 == HATE[u][i][1] and item2 == HATE[u][i][0]):
            return True
    return False
            

def oppose(R, item, u):

    for i in range(0, len(R)):
        if opposes(item, R[i], u):
            del R[:]
            return True
    return False


def invoke(item, R, u):
    if len(R) == 0:
        R.append(item)
    else:
        if (not combine(R, item, u)) and (not oppose(R, item, u)):
            R.append(item)


def printit(R):
    s = ""
    for i in range(0, len(R)):
        s += R[i] + ", "
    return s[:-2]


f = open("magicka.out", "w")

for u in range(0, t):
    RESULT = []

    for i in range(0, N[u]):
        invoke(LIST[u][i], RESULT, u)

    f.write("Case #" + str(u + 1) + ": [" + printit(RESULT) + "]\n")


f.close()

print "done"






















