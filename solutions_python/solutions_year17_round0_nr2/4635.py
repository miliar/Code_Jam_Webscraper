def is_sorted(s):
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return False
    return True


def solve(n):
    if n < 10:
        return n
    s = str(n)
    l = len(s)
    last = 0
    if is_sorted(s):
        return n
    for i in range(1, l):
        if s[i] <= s[i-1]:
            pos = i
            break
    fixed = str(int(s[:pos]) - 1)
    return int(fixed + '9' * (l - pos))


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print('Case #{}: {}'.format(i + 1, solve(int(input()))))
