def solve2(servers):
    res = 0
    for server in servers:
        last = ""
        for word in server:
            pos = 0
            while pos < len(last) and pos < len(word) and last[pos] == word[pos]:
                pos += 1
            res += len(word) - pos
            last = word
    return res + len(servers)

def solve(testNum):
    m, n = map(int, input().split())
    words = []
    for i in range(m):
        words.append(input())
    words.sort()
    nmask = n ** m
    res = 0
    cnt = 0
    for mask in range(nmask):
        cmask = mask
        servers = [[] for i in range(n)]
        for word in words:
            serv = cmask % n 
            cmask //= n
            servers[serv].append(word)
        good = True
        for server in servers:
            good = good and server
        if not good:
            continue
        nres = solve2(servers)
        if res == nres:
            cnt += 1
        elif res < nres:
            res = nres
            cnt = 1
    cnt %= 10**9 + 7
    print("Case #{}: {} {}".format(testNum, res, cnt))

   
t = int(input())
for i in range(t):
    solve(i + 1)    
