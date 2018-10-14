def inp():
    t = int(input())
    cases = []
    for i in range(t):
        d, n = [int(x) for x in input().split()]
        horses = []
        for j in range(n):
            horse = tuple(int(x) for x in input().split())
            horses.append(horse)
        cases.append((d, horses))
    return cases


def process(d, horses):
    m = (d - horses[0][0]) / horses[0][1]
    for horse in horses[1:]:
        t = (d - horse[0]) / horse[1]
        if t > m:
            m = t
    return d / m


cases = inp()
for i, case in enumerate(cases):
    print("Case #{}: {:.6f}".format(i+1, process(*case)))
