from sys import stdin

def checkit(strs):
    fprint = ['0' for c in range(0, 200)]
    s = strs[0]
    i = 0
    first = True
    for c in s:
        if first or c != pre:
            fprint[i] = c
            pre = c
            i += 1
            first = False
    fprint = ''.join(fprint).strip('0')
    total = []
    bad = False
    for s in strs:
        first = True
        nb = 0
        i = 0
        bad = False
        stuff = []
        for c in s:
            if c == fprint[i]:
                if first:
                    first = False
                else:
                    nb += 1
            else:
                stuff.append(nb)
                if first:
                    bad = True
                    break
                i += 1
                if i < len(fprint) and c == fprint[i]:
                    nb = 0
                else:
                    bad = True
                    break
        if bad:
            break
        stuff.append(nb)
        total.append(stuff)
    if i < len(fprint) - 1:
        bad = True
    if bad:
        print('Fegla Won')
    else:
        avg = [0 for x in total[0]]
        for stuff in total:
            for i in range(0, len(stuff)):
                avg[i] += stuff[i]
        for i in range(0, len(avg)):
            avg[i] = int(avg[i] / len(total))
        nb = 0
        for stuff in total:
            for i in range(0, len(stuff)):
                nb += abs(stuff[i] - avg[i])
        print(nb)

t = int(stdin.readline())
for i in range(0, t):
    n = int(stdin.readline())
    ss = [stdin.readline().strip() for i in range(0, n)]
    print('Case #{}: '.format(i+1), end='')
    checkit(ss)
