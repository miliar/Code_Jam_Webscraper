import sys

IMPOSSIBLE = 1000000000
mem = {}
hits = 0

def dist(a, b, i, j):
    global hits
    if (a, b, i, j) in mem:
        hits += 1
        return mem[(a, b, i, j)]
    if i >= len(a) and j >= len(b):
        return 0
    if i >= len(a) or j >= len(b):
        return IMPOSSIBLE
    if a[i] == b[j]:
        curi, curj = i, j
        res = IMPOSSIBLE
        if len(a) - i >= 2:
            if a[i] == a[i+1]:
                res = min(res, 1 + dist(a, b, i+1, j))
        if len(b) - j >= 2:
            if b[j] == b[j+1]:
                res = min(res, 1 + dist(a, b, i, j+1))
        res = min(res, dist(a, b, i+1, j+1))
        mem[(a, b, i, j)] = res
        return res
    if a[i] != b[j]:
        mem[(a, b, i, j)] = IMPOSSIBLE
        return IMPOSSIBLE
    

n_cases = int(sys.stdin.readline())
for i in range(n_cases):
    n_strings = int(sys.stdin.readline())
    strings = []
    for j in range(n_strings):
        strings.append(sys.stdin.readline().strip())
    best = dist(strings[0], strings[1], 0, 0)
    if best < IMPOSSIBLE:
        print("Case #" + str(i+1) + ": " + str(best))
    else:
        print("CASE #" + str(i+1) + ": Fegla Won")
    #print(dist(strings[0], strings[1], 0, 0))
    #print("Hits: " + str(hits))
