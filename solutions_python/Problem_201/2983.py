import sys


def place_next(s):
    j = 0
    ls = 0
    rs = 0
    ms = 0
    for i in range(1, len(s)):
        if s[i]:
            continue

        # calc left
        k = i
        while k > 0 and not s[k]:
            k -= 1
        a = i - k - 1

        # calc right
        k = i
        while k < len(s) and not s[k]:
            k += 1
        b = k - i - 1

        # check max
        if min(a, b) > ms:
            j = i
            ls = a
            rs = b
            ms = min(a, b)
        elif min(a, b) == ms and max(a, b) > ms:
            j = i
            ls = a
            rs = b
            ms = min(a, b)

    return j, ls, rs


def solve(n, k):
    stalls = [False]*(n+2)
    stalls[0] = True
    stalls[-1] = True

    ls, rs = 0, 0
    for i in range(k):
        j, ls, rs = place_next(stalls)
        stalls[j] = True

    return ls, rs


def main():
    t = sys.stdin.readline().strip()
    for i in range(int(t)):
        line = sys.stdin.readline().strip().split()
        a, b = solve(int(line[0]), int(line[1]))
        print("Case #{}: {} {}".format(i+1, max(a, b), min(a, b)))


if __name__ == '__main__':
    main()
