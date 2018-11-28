from sys import stdin

T = int(stdin.readline())

for t in range(1, T+1):
    L, P, C = map(int, stdin.readline().split())
    cexp = C
    ratio = 1.0*P/L
    counter = 0
    while cexp < ratio:
        counter += 1
        cexp = cexp*cexp
    print "Case #%d: %d" % (t, counter)
