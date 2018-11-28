

def check(l):
    j = len(l)

    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            j = i
            break

    for i in range(len(l)):
        if i + j + 1 >= len(l):
            break

        l[i + j + 1] = 9

    return l, j


def solve(N):
    l = list(map(int, str(N)))

    l, j = check(l)
    while j < len(l):
        i = 0
        while j - i >= 0:
            l[j - i] -= 1
            if l[j - i] == -1:
                l[j - i] = 9
                i += 1
            else:
                break

        l, j = check(l)

    return int(''.join(map(str, l)))


if __name__ == '__main__':
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for i in range(1, T + 1):
        N = int(f.readline())
        print("Case #{}: {}".format(i, solve(N)))
