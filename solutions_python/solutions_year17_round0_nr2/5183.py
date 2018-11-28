import sys


def get_last_tidy(n):
    n = int(n)
    if n < 10:
        return n

    for i in range(n, 0, -1):
        s = str(i)
        tidy = True

        for j in range(len(s) - 1):
            if s[j] > s[j + 1]:
                tidy = False
                break

        if tidy:
            return i


if __name__ == '__main__':
    sys.stdin.readline()

    i = 1
    for ln in sys.stdin:
        print("Case #{}: {}".format(i, get_last_tidy(ln)))
        i += 1