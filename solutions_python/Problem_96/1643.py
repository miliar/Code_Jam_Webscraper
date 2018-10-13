import math

T = input()

for k in range(1,T+1):
    numbers = map(int, raw_input().split())
    N = numbers.pop(0)
    S = numbers.pop(0)
    p = numbers.pop(0)
    scores = numbers
    found = 0
    vectors = []
    for g in scores:
        a = int(math.ceil(g/3.))
        b = int(math.ceil((g-a)/2.))
        c = g-a-b
        if max([a,b,c]) >= p:
            found += 1
        else:
            vectors.append([a,b,c])
    while S and vectors:
        a,b,c=vectors.pop()
        a, b, c = reversed([a-2, b+1, c+1])
        if min(a,b,c) < 0 or max(a,b,c) > 10 or c-a > 2:
            a, b, c = a-1, b, c+1
        if min(a,b,c) < 0 or max(a,b,c) > 10 or c-a > 2:
            continue
        if max(a,b,c) >= p:
            S -= 1
            found += 1
    print "Case #%d: %s" % (k, found)
