import math, sys

def is_tidy(N):
    N = str(N)
    pairs = [(N[i], N[i+1]) for i in range(len(N)-1)]

    return all(x[0] <= x[1] for x in pairs)

def solve(N):
    target = N
    K = int(math.floor(math.log(N)))

    for k in range(K+1):
        m = int(math.pow(10,k))

        if is_tidy(target):
            return target
        else:
            rest = (target / m)
            ld = rest % 10

            rest = rest - ld - 1

            target = rest * m + (m-1)


if __name__ == "__main__":
    sys.stdin = open('B-large.in')
    sys.stdout = open('out.txt', 'w')

    T = int(raw_input())


    for t in range(T):
        N = int(raw_input())

        print "Case #%d: %s" % (t + 1, solve(N))
