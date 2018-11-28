t = int(input())
for tst in range(t):
    def notpcake(pcake):
        if pcake == '+':
            return '-'
        return '+'
    p, k = input().split()
    k = int(k)
    p = list(p)
    flips = 0
    for idx, pancake in enumerate(p):
        if idx + k > len(p):
            break
        if pancake == '-':
            flips += 1
            for i in range(k):
                p[idx + i] = notpcake(p[idx + i])
    if '-' in p:
        res = "IMPOSSIBLE"
    else:
        res = flips
    print("Case #" + str(tst + 1) + ":", res)
