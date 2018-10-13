#! /usr/bin/env python3

for test in range(1, int(input()) + 1):
    n = [int(c) for c in reversed(input())]
    for i in range(len(n) - 1):
        if n[i] < n[i + 1]:
            for j in range(i + 1):
                n[j] = 9
            n[i + 1] -= 1
    while n[-1] == 0:
        n.pop()
    print('Case #{}: {}'.format(test, ''.join(str(c) for c in reversed(n))))
