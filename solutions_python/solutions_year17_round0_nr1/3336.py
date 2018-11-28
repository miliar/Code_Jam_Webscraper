import sys
sys.setrecursionlimit(1500)
#sys.stdin = open("a1.in")


def f(s, k):
    n = len(s)
    for i in range(n):
        if s[i] == "-":
            if i + k - 1 > n - 1:
                return False, 0
            else:
                l = list(s)
                for j in range(i, i + k):
                    if l[j] == "-":
                        l[j] = "+"
                    else:
                        l[j] = "-"
                t = "".join(l)
                p, m = f(t, k)
                if p:
                    return True, m + 1
                else:
                    return False, 0
    return True, 0

T = input()
T = int(T)
for t in range(1, T + 1):
    s, k = input().split()
    k = int(k)
    p, m = f(s, k)
    if p:
        res = m
    else:
        res = "IMPOSSIBLE"
    print("Case #" + str(t) + ": " + str(res))
