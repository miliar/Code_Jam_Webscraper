import sys

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
NbTests = int(input())  # read a line with a single integer
lsN = []
lsK = []
for i in range(NbTests):
    n, m = str(sys.stdin.readline()).replace('\n', '').split()
    lsN.append(int(n))
    lsK.append(int(m))

listeEspaces = []

def initL(nb):
    global listeEspaces
    listeEspaces = [[nb, 1]]

def install():
    global listeEspaces
    curr = listeEspaces[0]
    temp = curr[0] - 1
    card = curr[1]
    if temp % 2 == 0:
        a = temp // 2
        #print(a, listeEspaces[-1][0])
        if listeEspaces[-1][0] == a:
            listeEspaces[-1][1] += 2 * card
        else:
            listeEspaces.append([a, 2 * card])
    else:
        b = temp // 2
        a = temp - b
        if listeEspaces[-1][0] == a:
            listeEspaces[-1][1] += card
        else:
            listeEspaces.append([a, card])
        listeEspaces.append([b, card])
    listeEspaces.pop(0)
    #print(listeEspaces)
    return temp, card



def StallFunction(nbStalls, nbPersons):
    global listeEspaces
    initL(nbStalls)
    temp = 0
    #print(listeEspaces)
    i = 0
    temp = nbStalls
    while i < nbPersons:
        temp, card = install()
        i += card
    m = temp // 2
    M = temp - m
    return m, M

for i in range(1, NbTests + 1):
    m, M = StallFunction(lsN[i-1], lsK[i-1])
    print("Case #{}: {} {}".format(i, M, m))
  # check out .format's specification for more formatting options
