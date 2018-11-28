import sys


def war(N, NB, KB):
    KB_copy = KB[:]
    for i in range(N):
        for j in range(N):
            if KB_copy[j] and KB_copy[j] > NB[i]:
                KB_copy[j] = None
                break

    return len([i for i in KB_copy if i])


def solve(N, NB, KB):
    war_result = war(N, NB, KB)
    dwar_result = war(N, KB, NB)
    return (war_result, N - dwar_result)


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            N = int(f.readline().strip())
            NB = sorted([float(v) for v in f.readline().strip().split()])
            KB = sorted([float(v) for v in f.readline().strip().split()])
            result = solve(N, NB, KB)
            print "Case #%d: %s %s" % (t+1, result[1], result[0])


if __name__ == "__main__":
    main(sys.argv[1])
