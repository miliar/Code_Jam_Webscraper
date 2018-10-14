import sys
import math


DEBUG=True if len(sys.argv) > 1 else False

def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def solve(N, K):
    # Generation
    g = math.floor(math.log2(K))

    # Number in the current generation (equals total of previous generations plus 1)
    p = pow(2,g)

    # Remaining available stalls
    r = N - p + 1
    # Size of each of the largest available spaces for the current generation
    s = math.ceil(r/p)
    # Size of smallest available spaces for the current generation
    ss = s - 1

    # Number of elements of the first class (if 2 classes for this generation, else this number equals the number of elements in the generation)
    c = r + p * (1 - s)

    # If K is in the first class, i.e. falls in one of the largest spaces
    if K - p + 1 <= c:
        mx = math.floor(s / 2)
        if s % 2 == 0:
            mn = max(mx - 1, 0)
        else:
            mn = mx
    # Second class
    else:
        mx = math.floor(ss / 2)
        if ss % 2 == 0:
            mn = max(mx - 1, 0)
        else:
            mn = mx

    debug("g:", g, "p:", p, "s:", s, "r:", r, "c:", c, "mx:", mx, "mn:", mn)

    return mx, mn



for case in range(1, int(sys.stdin.readline())+1):
    N, K = map(int, sys.stdin.readline().split())

    debug("N:", N, "K:", K)

    mx, mn = solve(N, K)

    print("Case #{0}: {1} {2}".format(case, mx, mn))


#for case in range(1, int(sys.stdin.readline())+1):
#    K, C, S = map(int, sys.stdin.readline().split())

