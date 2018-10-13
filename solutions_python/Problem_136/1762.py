import sys

sys.stdin = open('B-small-attempt0.in')
sys.stdout = open('2.out', 'w')

N = int(input())

for case in range(N):
    (C, F, X) = [float(x) for x in input().split()]
    minT = X/2
    n = 0
    while True:
        n += 1
        nMin = (X)/(n*F + 2)
        for i in range(n):
            nMin += (C) / (2 + i*F)

        if nMin < minT:
            minT = nMin
        else:
            break
    print("Case #{}: {}".format(case + 1, minT))
sys.stdout.close()
