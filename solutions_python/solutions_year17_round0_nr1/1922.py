
def checkComplete(s):
    for l in s:
        if l != '+': return False
    return True

def generateChildren(s, k, d):
    children = []
    for i in range(len(s)-k+1):
        child = revert(s, i, i+k-1)
        if(child not in d): children.append(child)
    return children

def revert(s, start, end):
    ans = ""
    for i, l in enumerate(s):
        if i < start or i > end:
            ans += l
            continue
        elif l == '+':
            ans += '-'
        elif l == '-':
            ans += '+'
    return ans

import queue
T = int(input())
for i in range(1,T+1):
    linesplit = input().split(" ")
    S = linesplit[0]
    K = int(linesplit[1])

    existing = dict()
    q = queue.Queue()
    q.put( (S, 0) )
    possible = False

    while(not q.empty()):
        strng, steps = q.get()
        if strng in existing: continue
        existing[strng] = True
        if checkComplete(strng):
            print("Case #{}: {}".format(i, steps))
            possible = True
            break
        else:
            children = generateChildren(strng, K, existing)
            for c in children:
                newTuplee = (c, steps+1)
                q.put(newTuplee)
    if not possible:
        print("Case #{}: IMPOSSIBLE".format(i))
