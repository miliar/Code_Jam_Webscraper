import sys

sys.stdin = open("A-large.in", "r")
sys.stdout = open("sol", "w")

T = int(input())

for t in range(T):
    p, K = input().split()
    p = list(p)
    K = int(K)

    flips = 0
    for i in range(len(p) - K + 1):
        if p[i] == '-':
            for j in range(i, i+K):
                if p[j] == '-':
                    p[j] = '+'
                else:
                    p[j] = "-"

            flips += 1

    good = True
    for i in p:
        if i != '+':
            good = False
            break

    if good:
        print("Case #" + str(t + 1) + ":", flips)
    else:
        print("Case #" + str(t + 1) + ":", "IMPOSSIBLE")