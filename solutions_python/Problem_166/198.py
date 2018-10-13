from itertools import permutations, product

def oc(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
def solve(k, l, s, a, b):
    tot = 0
    totc = 0
    mm = -1
    ll = []
    for p in product(a, repeat=s):
        s = ''.join(p)
        c = oc(s, b)
        totc = totc + c
        mm = max(mm, c)
        tot = tot + 1
    return 1.0 * mm - (1.0 * totc / (1.0 * tot))
for tc in range(int(input())):
    M = map(int, raw_input().split())
    a = raw_input()
    b = raw_input()
    print "Case #%d: %.7f" % (tc + 1, solve(M[0], M[1], M[2], a, b))

