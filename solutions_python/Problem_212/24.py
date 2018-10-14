
def run_test():
    N, P = map(int, input().split())
    G = [int(x) for x in input().split()]
    assert len(G) == N
    d = {0:0, 1:0, 2:0, 3:0}
    for g in G:
        d[g%P] += 1

    if P == 2:
        return d[0] + (d[1] + 1) // 2
    elif P == 3:
        ans = d[0]
        sm, lg = min(d[1], d[2]), max(d[1], d[2])
        ans += sm
        ans += (lg - sm + 2) // 3
        return ans
    elif P == 4:
        ans = d[0]
        sm, lg = min(d[1], d[3]), max(d[1], d[3])
        md = d[2]
        ans += md // 2
        md = md % 2
        ans += sm
        sm, lg = 0, lg - sm
        if lg % 4 == 0:
            ans += lg // 4 + md
        elif lg % 4 == 1:
            ans += lg // 4 + 1
        elif lg % 4 == 2:
            ans += lg // 4 + 1
        elif lg % 4 == 3:
            ans += lg // 4 + 1 + md
        return ans

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))
