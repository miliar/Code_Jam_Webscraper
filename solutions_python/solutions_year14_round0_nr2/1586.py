import math, itertools


def solve(C, F, X):
    def cost(r):
        # Calculate time with r farms
        #   = (sum C/(2+iF) for i = 0 to r-1) + X/(2 + rF)
        return math.fsum(itertools.chain((C/(2 + i*F) for i in range(r)),
            [X/(2 + r*F)]))

    r = max(0, int(X/C - 2/F)) # Solve cost(r) - cost(r-1) = 0
    return cost(r)


def main():
    T = int(input())
    for tc in range(T):
        C, F, X = map(float, input().split())
        print("Case #{}: {:.7f}".format(tc + 1, solve(C, F, X)))


if __name__ == "__main__":
    main()
