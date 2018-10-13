import sys
stdin = sys.stdin

sys.setrecursionlimit(3000)


INF = 2147483647


T = int(stdin.readline())
for icase in range(T):
    N, X = map(int, stdin.readline().strip().split())
    ns = map(int, stdin.readline().strip().split())

    ns.sort()
    ns.reverse()
    re = 0
    used = [False] * N
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        for k in range(i+1, N):
            if not used[k] and ns[i] + ns[k] <= X:
                used[k] = True
                break
        re += 1

        
    print "Case #%d:" % (icase+1), re
    sys.stdout.flush()


