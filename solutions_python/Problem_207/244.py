# Stable Neigh-bors

def solve(n, unicorns):
    colors = ['R', 'O', 'Y', 'G', 'B', 'V']
    ndef = {}
    for i in range(6):
        ndef[colors[i]] = [colors[(i + 1) % 6], colors[i], colors[(i + 5) % 6]]
        nb = unicorns[(i + 1) % 6] + unicorns[(i + 5) % 6]
        loop = n if nb == 0 else n - nb - 1
        if unicorns[i] > 1 and unicorns[i] * 2 > loop:
            return "IMPOSSIBLE"
    num = [[-u, c] for (u, c) in zip(unicorns, colors)]
    num.sort()
    num[0][0] -= 0.5
    ret = ''
    neighbors = []
    for i in range(n):
        num.sort()
        for j in range(6):
            if not num[j][1] in neighbors:
                if num[j][0] > -1:
                    print "ERROR"
                ret += num[j][1]
                num[j][0] += 1
                neighbors = ndef[num[j][1]]
                break
    if ret[0] == ret[-1]:
        print "ERROR2"
    return ret

cases = int(raw_input())
for case in range(1, cases + 1):
    unicorns = map(int, raw_input().split(' '))
    print "Case #" + str(case) + ": " + solve(unicorns[0], unicorns[1:])
