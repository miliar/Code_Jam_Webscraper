def solve(s):
    if len(s) == 1: return s
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            while i and s[i - 1] == s[i]: i -= 1
            if i == 0 and s[0] == '1':
                return '9' * (len(s) - 1)
            return s[:i] + chr(ord(s[i]) - 1) + '9' * (len(s) - i - 1)
    return s

for i in range(1, int(input()) + 1):
    print("Case #", i, ": ", solve(input()), sep='')

