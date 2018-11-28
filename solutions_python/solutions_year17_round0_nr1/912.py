from collections import deque
def flip(symbol):
    if symbol == '+':
        return '-'
    else:
        return '+'
def getFlipped(vertex,n,i,j):
    newVertex = ""
    k = 0
    while k < n:
        if k >= i and k <= j:
            newVertex += flip(vertex[k])
        else:
            newVertex += vertex[k]
        k += 1
    return newVertex
def isFinalState(v,n):
    i = 0
    j = n-1
    while i<=j:
        if v[i] != '+' or v[j] != '+':
            return False
        i += 1
        j -= 1
    return True

def dfs(sourceStr,n,k):
    if isFinalState(sourceStr,n):
        return 0
    shortestPaths = {}
    shortestPaths[sourceStr] = 0
    dfsQ = deque([])
    dfsQ.append(sourceStr)
    while dfsQ:
        vertex = dfsQ.popleft()
        i = 0
        j = k-1
        while j < n:
            adjV = getFlipped(vertex,n,i,j)
            if isFinalState(adjV,n):
                return shortestPaths[vertex] + 1
            if not shortestPaths.has_key(adjV):
                shortestPaths[adjV] = shortestPaths[vertex] + 1
                dfsQ.append(adjV)
            i += 1
            j += 1
    return "Impossible"

t = int(raw_input())
counter = 1
while counter <= t:
    stringInp,kStr = raw_input().split()
    k = int(kStr)
    n = len(stringInp)
    ans = dfs(stringInp,n,k)
    print "Case #" + str(counter) + ": " + str(ans)
    counter += 1
