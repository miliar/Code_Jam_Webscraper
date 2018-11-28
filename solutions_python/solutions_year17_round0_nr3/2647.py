import sys
import math


def solve1(N,K):
    t = N/K

def solve(N, K):
    n = [int(N)]
    for k in range(int(K)-1):
        t = max(n)
        n.remove(t)
        n.append(math.ceil((t - 1) / 2))
        n.append(math.floor((t - 1) / 2))
    t = max(n)
    if t > 1:
        return math.ceil((t-1)/2), math.floor((t-1)/2);
    else:
        return 0, 0

def main(infile, outfile):
    with open(infile, "rt") as f:
        T = int(f.readline())
        sol = []
        for t in range(1, T + 1):
            N, K = f.readline().split()
            ans1, ans2 = solve(N, K)
            sol.append("Case #{0}: {1} {2}\n".format(t, ans1, ans2))
        print(sol)
    with open(outfile, "wt") as f:
        f.writelines(sol)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

