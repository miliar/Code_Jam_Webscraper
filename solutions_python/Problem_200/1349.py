def is_tidy(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


def get_tidy_index(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return i


def calc(n, index):
    length = len(str(n))
    keta = 10 ** (length - (index + 1))
    return n // keta * keta - 1


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        while not is_tidy(N):
            idx = get_tidy_index(N)
            N = calc(N, idx)
        print("Case #{x}: {y}".format(x=t, y=N))