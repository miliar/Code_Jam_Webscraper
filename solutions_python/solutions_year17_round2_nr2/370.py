import sys

T = int(sys.stdin.readline())
for x in range(T):
    N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split())
    N2 = N // 2
    if R > N2 or Y > N2 or B > N2:
        res = "IMPOSSIBLE"
    else:
        res = ["X"] * N
        ns, cs = zip(*sorted(zip([R, Y, B], "RYB"), reverse=True))
        for i in range(ns[0]):
            j = i * 2
            res[j] = cs[0]

        cnt = 0
        j = N-1
        while True:
            if res[j] == 'X':
                res[j] = cs[1]
                cnt += 1
                j -= 1
            if cnt == ns[1]:
                break
            j -= 1

        for i in range(N):
            if res[i] == 'X':
                res[i] = cs[2]
        res = ''.join(res)

    print("Case #{}: {}".format(x+1, res))

