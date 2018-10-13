def firstLower(N):
    last = int(N[0])
    for i in range(1, len(N)):
        cur = int(N[i])
        if cur < last:
            return i
        last = cur
    return -1

def solve(N):
    l = firstLower(N)
    if l == -1:
        return N

    Nt = [x for x in N]
    cur = int(Nt[l - 1])
    if cur == 1:
        if l - 1 == 0:
            return ''.join(['9' for x in range(len(N) - 1)])
        Nt[l - 1:] = ['0' for x in range(len(N) - 1)]
        return solve(''.join(Nt))

    Nt[l - 1] = str(cur - 1)
    Nt[l:] = ['9' for x in range(len(N) - l)]
    return solve(''.join(Nt))



T = int(input())
for i in range(1, T+1):
    N = input()

    res = solve(N)
    #print("Case #{}: {} solves {}".format(i, res, N))
    print("Case #{}: {}".format(i, res))




