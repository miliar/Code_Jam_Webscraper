def tidy(n):
    return sorted(n) == list(n)


def solve(n):
    s = str(n)
    if tidy(s):
        return n

    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            break
    for j in range(i, 0, -1):
        if s[j-1] < s[j]:
            break
    else:
        j = 0
    s = s[:j] + str(int(s[j]) - 1) + '9' * (len(s) - j - 1)
    return int(s)


def test_solve():
    assert solve(132) == 129
    assert solve(21) == 19
    assert solve(1000) == 999
    assert solve(7) == 7
    assert solve(1) == 1
    assert solve(10) == 9
    assert solve(111111111111111110) == 99999999999999999
    assert solve(2209) == 1999
    assert solve(2319) == 2299


def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        print('Case #{}: {}'.format(i, solve(N)))


if __name__ == '__main__':
    main()
