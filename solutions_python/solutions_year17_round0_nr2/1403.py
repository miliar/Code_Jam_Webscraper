from itertools import combinations


def check(s):
    for i, c in enumerate(s):
        if i > 0 and ord(c) < ord(s[i - 1]):
            return False
    return True

def solve(n):
    s = str(n)
    if check(s):
        return n
    if len(s) == 1:
        return n
    q = sum([check(s[:i]) for i in range(1, len(s))])
    if s[q - 1] == '1':
        return int('9' * (len(s) - 1))
    w = s.find(s[q - 1])
    s = list(s)
    s[w] = chr(ord(s[w]) - 1)
    s = ''.join(s[:w + 1])
    s = s + '9' * (len(str(n)) - len(s))
    return int(s)

for i in range(int(input())):
    print('Case #' + str(i + 1)  + ':', solve(int(input())))

