
from collections import deque

T = int(raw_input())


def check(n):
    b = 10
    while n:
        d = n % 10
        if d <= b:
            b = d
        else:
            return False
        n = n // 10
    return True

def foo(n):
    while n:
        if check(n):
            return n
        n = n - 1


for t in range(T):
    line = raw_input()
    n = int(line)
    r = foo(n)
    if r is None:
        print("Case #{}: IMPOSSIBLE".format(t + 1))
    else:
        print("Case #{}: {}".format(t + 1, r))
