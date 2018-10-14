def getlr(x):
    x = x-1
    a = x//2
    b = x-a
    return max(a,b), min(a,b)

N = int(input())
for n in range(1, N+1):
    stalls, ppl = map(int, input().split())
    d = [stalls]
    a, b = 0, 0
    for _ in range(ppl):
        d.sort()
        x = d.pop(len(d)-1)
        a, b = getlr(x)
        d.append(a)
        d.append(b)
    print('Case #{}: {} {}'.format(n, a, b))
