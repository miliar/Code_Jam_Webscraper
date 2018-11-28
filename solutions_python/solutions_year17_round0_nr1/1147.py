import sys

def solve():
    line, k = raw_input().strip().split()
    k = int(k)
    result = 0

    swapped = False
    endings = set()
    for idx, c in enumerate(line):
        if idx in endings:
            endings.remove(idx)
            swapped = not swapped

        if (c == '+') == swapped:
            if idx + k > len(line):
                print "IMPOSSIBLE"
                return

            endings.add(idx + k)
            swapped = not swapped
            result += 1

    print result


if __name__ == '__main__':
    T = int(raw_input())
    for case_idx in xrange(1, T+1):
        sys.stdout.write("Case #{}: ".format(case_idx))
        solve()
