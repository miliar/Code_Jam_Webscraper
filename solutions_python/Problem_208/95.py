import sys

def get_ints(instrm):
    return [int(i) for i in instrm.readline().rstrip().split()]
    
def parse(instrm):
    n, _ = get_ints(instrm)
    horses = []
    for i in range(n):
        horses.append(get_ints(instrm))
    ds = []
    for i in range(n):
        toks = get_ints(instrm)
        if i < n - 1:
            ds.append(toks[i+1])
    instrm.readline()
    return horses, ds


def solve(case):
    horses, ds = case
    n = len(horses)
    dp = [[None]*n for _ in range(n)]
    dp[0][0] = (0, horses[0][0])
    for i in range(1, n):
        d = ds[i-1]
        min_time = None
        for h in range(i):
            if dp[i-1][h] is None or dp[i-1][h][1] < d: continue
            dp[i][h] = (dp[i-1][h][0] + d/horses[h][1], dp[i-1][h][1] - d)
            if min_time is None or min_time > dp[i][h][0]:
                min_time = dp[i][h][0]
        dp[i][i] = (min_time, horses[i][0])
    
    return min_time


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
