#!/usr/bin/python3

def prey(x):
    l = list(map(int, list(str(x))))
    for q in range(20):
        i = 1
        while i < len(l):
            if l[i] < l[i - 1]:
                break
            i += 1
        if i == len(l):
            break
        l[i - 1] -= 1
        for j in range(i, len(l)):
            l[j] = 9
    return int(''.join(list(map(str, l))))

def solve():
    T = int(input())
    for t in range(T):
        n = int(input())
        print('Case #{}: {}'.format(t + 1, prey(n)))

solve()
