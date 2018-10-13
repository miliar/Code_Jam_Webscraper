def is_tidy(x):
    s = str(x)
    return all(c <= s[i] for i, c in enumerate(s[:-1], 1))


def not_dec(s):
    for i, c in enumerate(s[:-1]):
        if c > s[i+1]:
            return i, s[i+1]
    return i, 'x'


def solve(x):
    """Return the largest tidy number <= x"""
    if n <= 1000:
        for i in range(x, 1, -1):
            if is_tidy(i):
                return i
        return 1
    else:
        ss = list(str(x))
        i, c = not_dec(ss)
        while i < len(ss):
            ss[i] = c
            if all(s == '0' for s in ss):
                return '9' * (len(ss) - 1)
            i, c = not_dec(ss)
        return "".join(ss)


if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        ans = solve(n)
        print("Case #{}: {}".format(t+1, ans))
