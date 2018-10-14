from sys import stdin

def riadok():
    return map(int, stdin.readline().split())

for cas in range(int(stdin.readline())):
    inp = riadok()
    N, S, p = inp[:3]
    res = 0
    for t in inp[3:]:
        b = (t + 2) / 3
        if b >= p:
            res += 1
        elif (t + 4) / 3 >= p and p > 1 and S > 0:
            res += 1
            S -= 1
    print "Case #%d: %d" % (cas + 1, res)
