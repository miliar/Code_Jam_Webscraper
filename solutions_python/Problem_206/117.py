import sys


def parse(instrm):
    d, n = [int(i) for i in instrm.readline().rstrip().split()]
    others = []
    for i in range(n):
        start, speed = [int(i) for i in instrm.readline().rstrip().split()]
        others.append((start, speed))
    return d, others


def solve(case):
    d, others = case
    time = 0
    for start, speed in others:
        t = (d - start)/speed
        time = max(t, time)
    return d/time


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
