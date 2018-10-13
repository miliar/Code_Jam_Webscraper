import re


def solve(s, k):
    s_set = set(s)
    s_len = len(s)
    if s_set == {'+'}:
        return 0
    if s_set == {'-'} and s_len % k == 0:
        return int(s_len / k)
    count = 0
    if s.startswith('+'):
        s = re.sub(r"\++-", '-', s, 1)
    while len(s) >= k and set(s) != {'+'}:
        s0, s1 = list(s[:k]), s[k:]
        for i in range(k):
            s0[i] = '+' if s0[i] == '-' else '-'
        count += 1
        s = ''.join(s0) + s1
        if s.startswith('+'):
            s = re.sub(r"\++-", '-', s, 1)
    if set(s) == {'+'}:
        return count
    return "IMPOSSIBLE"


t = int(input())
for i in range(1, t + 1):
    s, k = input().split(" ")
    print("Case #{}: {}".format(i, solve(s, int(k))))
