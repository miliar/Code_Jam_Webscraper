from sys import stdin, stdout
from math import pi

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    N,K = map(int, stdin.readline().strip().split())
    pancakes = [tuple(map(int, stdin.readline().strip().split())) for i in range(N)]

    pancakes.sort(key=lambda x: x[0]*x[1], reverse=True)
    big = pancakes[:K]
    # big.sort(key=lambda x:x[0], reverse=True)
    bigmax = max(big, key=lambda x:x[0])
    wide = []
    for r,h in pancakes[K:]:
        if r > bigmax[0]:
            wide.append( (r,h) )

    subtotal = 0
    for r,h in big[:-1]:
        subtotal += r*h

    total = 2*pi*(subtotal + big[-1][0]*big[-1][1]) + pi*bigmax[0]**2

    for r,h in wide:
        total = max(2*pi*(subtotal + r*h) + pi*r**2, total)

    stdout.write("Case #{:d}: {:f}\n".format(case_num, total))
