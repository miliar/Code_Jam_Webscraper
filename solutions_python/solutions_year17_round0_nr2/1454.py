#!/usr/bin/python3

def ok(s):
    if isinstance(s, int):
        s = str(s)
    for i in range(len(s) - 1):
        if ord(s[i]) > ord(s[i + 1]):
            return False
    return True


def is_in_range(l, r):
    s = str(l)
    t = str(r)
    w = s[0]
    while len(w) < len(s):
        if w == s[:len(w)]:
            w += chr(max(ord(w[-1]), ord(s[len(w)])))
        else:
            w += w[-1]
    return int(s) <= int(w) <= int(t)
    

def solve(t):
    n = int(input())
    l, r = 1, n + 1
    while l < r - 1:
        mid = (l + r) >> 1
        if is_in_range(mid, n):
            l = mid
        else:
            r = mid
    print("Case #{}: {}".format(t, l))
    

n_o_t = int(input())
for i in range(n_o_t):
    solve(i + 1)
