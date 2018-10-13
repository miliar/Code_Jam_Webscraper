import sys


def parse(instrm):
    return instrm.readline().rstrip()


def solve(seq):
    seq = [int(c) for c in seq]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i] -= 1
                for j in range(i+1, len(seq)):
                    seq[j] = 9
                sorted = False
                break
    start = 0
    while start < len(seq) - 1 and seq[start] == 0:
        start += 1
    return "".join(str(n) for n in seq[start:])


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
