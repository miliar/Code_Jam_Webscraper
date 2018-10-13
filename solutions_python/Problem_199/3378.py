import sys

def case(n, s):
    print("Case #" + str(n+1) + ": " + s)

def flip(table, p):
    table2 = table.copy()
    for j in range(p, p+K):
        table2[j] = not table2[j]
    return(table2)

def explore(table, depth):
    #print(table, depth)
    if not False in table:
        global minDepth
        if depth < minDepth:
            minDepth = depth
        return False
    if depth > 11 or depth > minDepth:
        return False
    for k in range(len(table)-K+1):
        if False in table[k:k+2] and not table[k] == True and not table[k] == True:
            newTable = flip(table, k)
            explore(newTable, depth+1)

Input = open("A-small-attempt2.in", "r")

N = int(Input.readline()[:-1])
for i in range(N):
    table, K = [t for t in Input.readline()[:-1].split()]
    K = int(K)
    table = [p == "+" for p in table]
    minDepth = 500
    explore(table, 0)

    if minDepth == 500:
        case(i, "IMPOSSIBLE")
    else:
        case(i, str(minDepth))
