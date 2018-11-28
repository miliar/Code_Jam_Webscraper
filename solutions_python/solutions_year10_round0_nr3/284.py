import sys
T = input()
for t in range(1, T + 1):
    d = {}
    sys.stdout.write('Case #%d: ' % t)
    R, k, N = map(int, raw_input().split())
    g = map(int, raw_input().split())
    offset = 0
    if sum(g) <= k:
        print R * sum(g)
    else:
        earn = [0] * N
        next = [0] * N
        on_board = 0
        end = 0
        for i in range(N):
            while on_board + g[end] <= k:
                on_board += g[end]
                end = (end + 1) % N
            earn[i] = on_board
            next[i] = end
            on_board -= g[i]
        ans = 0
        cur = 0
        while R > 0:
            ans += earn[cur]
            cur = next[cur]
            R -= 1
        print ans


