import math, sys

def get_max_space(N, K):
    return math.ceil((N-K+1) / math.pow(2, math.floor(math.log(K)/math.log(2))))

def solve(N, K):

    space = get_max_space(N, K)

    maxL = math.ceil((space-1) / 2)
    minL = math.floor((space-1) / 2)

    return (maxL, minL)


if __name__ == "__main__":
    sys.stdin = open('C-small-2-attempt0.in')
    sys.stdout = open('out.txt', 'w')

    T = int(raw_input())


    for t in range(T):
        N, K = [int(x) for x in raw_input().split(" ")]

        maxL, minL = solve(N, K)

        print "Case #%d: %d %d" % (t + 1, maxL, minL)
