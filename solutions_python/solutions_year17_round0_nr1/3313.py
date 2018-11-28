def flip(s, k, start):
    for i in range(start, start + k):
        if s[i] == '+':
            s[i] = '-'
        else:
            s[i] = '+'


def is_minus_seq(s, k, start):
    for i in range(start, start + k):
        if s[i] != '-':
            return False
    return True


def is_plus_seq(s, k, start):
    for i in range(start, start + k):
        if s[i] != '+':
            return False
    return True


def solve(s, k, start, times):
    # print("étape", times, ":", s)
    if start + k > len(s):
        return times

    if is_minus_seq(s, k, start):
        flip(s, k, start)
        return solve(s, k, start + k, times + 1)

    if s[start] == '-':
        if start + 1 + k > len(s):
            return times

        j = start + 1
        while j + k <= len(s) and not is_minus_seq(s, k, start):
            flip(s, k, j)
            j += 1

        if is_minus_seq(s, k, start):
            flip(s, k, start)
            return solve(s, k, start + k, times + j - start)
        else:
            return times + 1

    return solve(s, k, start + 1, times)


T = int(input())
for i in range(T):
    s, k = (s for s in input().split())
    s = list(s)
    k = int(k)
    res = solve(s, k, 0, 0)
    if is_plus_seq(s, len(s), 0):
        print("Case #{}: {}".format(i + 1, res))
    else:
        print("Case #{}: IMPOSSIBLE".format(i + 1))
