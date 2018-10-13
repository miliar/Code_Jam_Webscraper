import sys


def solution(pankakes, K):
    flips = 0
    for i in range(len(pankakes)):
        if pankakes[i] == "-":
            flips += 1
            for f in range(i, i + K):
                try:
                    pankakes[f] = "+" if pankakes[f] == "-" else "-"
                except IndexError:
                    return "IMPOSSIBLE"
    return flips


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        pankakes, K = sys.stdin.readline().strip().split(" ")
        print "Case #%d: %s" % (i + 1, solution([p for p in pankakes], int(K)))
