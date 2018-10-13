from operator import xor


T = int(raw_input())

for t in range(T):
    N = int(raw_input())
    Cs = map(int, raw_input().split(' '))

    if not reduce(xor, Cs):
        sean = sum(Cs) - min(Cs)
    else:
        sean = "NO"

    print "Case #%d: %s" % (t+1, sean)
