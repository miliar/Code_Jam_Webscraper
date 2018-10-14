def compute(S):
    total = sum(S)
    extra = 0
    up = 0
    at = 0

    first = True
    while up < total:
        if not first:
            extra += 1
            up += 1
            total += 1
        first = False
        while at <= up and up < total:
            up += S[at]
            at += 1

    return extra

t = int(input())
for i in range(t):
    m, d = input().split(" ")
    S = list(map(int, list(d)))
    print("Case #%d: %d" % (i + 1, compute(S)))
