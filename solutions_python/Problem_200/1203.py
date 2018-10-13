import sys

def solve():
    line = map(int, list(raw_input().strip()))
    line.reverse()
    cur = 9
    for i, v in enumerate(line):
        if v > cur:
            line[i] -= 1
            line[:i] = [9] * i
        cur = line[i]

    if line[-1] == 0:
        line.pop()

    line.reverse()
    return "".join(map(str, line))


if __name__ == '__main__':
    T = int(raw_input())
    for case_idx in xrange(1, T+1):
        sys.stdout.write("Case #{}: ".format(case_idx))
        print solve()
