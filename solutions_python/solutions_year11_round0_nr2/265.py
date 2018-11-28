import sys
from collections import defaultdict

n = int(input())
for case in range(1, n+1):
    combos = {}
    destructos = defaultdict(set)

    line = input()
    token = list(reversed(line.split()))

    C = int(token.pop())
    for _ in range(C):
        a,b,c = token.pop()
        combos[a+b] = c
        combos[b+a] = c

    D = int(token.pop())
    for _ in range(D):
        a,b = token.pop()
        destructos[a].add(b)
        destructos[b].add(a)

    N = int(token.pop())
    s = token.pop()

    chars = []
    for i in range(N):
        c = s[i]
        chars.append(c)
        tail = "".join(chars[-2:])
        if tail in combos:
            chars[-2:] = [ combos[tail] ]
        elif len(destructos[c].intersection(set(chars))) > 0:
            chars = []

    print("Case #" + str(case) + ": [" + (", ".join(chars)) + "]")
