from string import maketrans

prev = set()
intab = "+-"
outtab = "-+"
trantab = maketrans(intab, outtab)

def flip(S, K, P):
    return(S[0:P] + S[P:P + K].translate(trantab) + S[P+K:])

def is_solvable(S, K, flips):
    if len(S) == S.count('+'):
        return (flips)
    if S in prev:
        return (0)
    prev.add(S)
    for i in range(0, len(S) - K + 1):
        real_flips = is_solvable(flip(S, K, i), K, flips + 1)
        if (real_flips > 0):
            return (real_flips)
    return (-1)

def solve(S, K, flips, max_flips, case):
    if len(S) == S.count('+'):
        print ("Case #{}: {}".format(case, flips))
        return (1)
    if flips > max_flips or S in prev:
        return (0)
    prev.add(S)
    for i in range(0, len(S) - K + 1):
        if solve(flip(S, K, i), K, flips + 1, max_flips, case):
            return (1)
        if not flips:
            prev.clear()
            prev.add(S)
    return (0)



lines = int(input())
for i in range(1, lines + 1):
    n, m = [s for s in raw_input().split(" ")]
    m = int(m)
    depth = is_solvable(n, m, 0)
    prev.clear()
    if depth >= 0:
        for x in range(1, depth + 2):
            if solve(n, m, 0, x, i):
                break
            prev.clear()
    else:
        print ("Case #{}: IMPOSSIBLE".format(i))
    prev.clear()
