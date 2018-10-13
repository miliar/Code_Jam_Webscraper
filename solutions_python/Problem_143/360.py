from sys import stdin, stdout


def solve(a, b, k):
    cnt = 0
    for old in range(0, a):
        for new in range(0, b):
            if (old & new) < k:
                cnt += 1
    return cnt


def main():
    lines = [l[:-1] for l in stdin.readlines()]

    t = int(lines[0])
    lines = lines[1:]

    for test in range(t):
        [a, b, k] = [int(x) for x in lines[0].split()]
        lines = lines[1:]
        print("Case #{}: {}".format(test + 1, solve(a, b, k)))

main()

