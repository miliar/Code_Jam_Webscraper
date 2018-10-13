import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))

for case in range(1, cases + 1):
    line = inp.pop(0).strip()
    N, P = map(int, line.split())

    line = inp.pop(0).strip()
    G = map(int, line.split())

    count = [0] * P
    for g in G:
        count[g % P] += 1

    result = count[0]
    count[0] = 0
    for i in range(1, P):
        pair = min(count[i], count[P-i])
        if i == P-i:
            pair = count[i] // 2
        result += pair
        count[i] -= pair
        count[P-i] -= pair

    if P == 4:
        if count[2] and count[1] >= 2:
            result += 1
            count[2] -= 1
            count[1] -= 2
        if count[2] and count[3] >= 2:
            result += 1
            count[2] -= 1
            count[3] -= 2

    for i in range(1, P):
        group = count[i] // P
        result += group
        count[i] -= P * group

    if sum(count):
        result += 1

    print 'Case #{}: {}'.format(case, result)
