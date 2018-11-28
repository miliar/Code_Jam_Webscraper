import itertools

def Check(s):
    result = True
    l = []
    for i in s:
        l.append(i)
    l2 = []
    while len(l) != 1:
        l2 = []
        for i in range(len(l) / 2):
            if l[i * 2] == l[i * 2 + 1]:
                l2.append(l[i*2])
                l2.append(l[i*2+1])
                result = False
                break
            else:
                if l[i * 2] == 'P' and l[i * 2 + 1] == 'R':
                    l2.append('P')
                elif l[i * 2] == 'P' and l[i * 2 + 1] == 'S':
                    l2.append('S')
                elif l[i * 2] == 'R' and l[i * 2 + 1] == 'P':
                    l2.append('P')
                elif l[i * 2] == 'R' and l[i * 2 + 1] == 'S':
                    l2.append('R')
                elif l[i * 2] == 'S' and l[i * 2 + 1] == 'P':
                    l2.append('S')
                elif l[i * 2] == 'S' and l[i * 2 + 1] == 'R':
                    l2.append('R')
        if len(l) % 2 == 1:
            l2.append(l[-1])
        if len(l) == len(l2):
            result = False
            break
        l = l2
    return result

def GetResult(N, L):

    result = ''

    if N > 1 and L[0] == 0 and L[1] == L[2]:
        return "IMPOSSIBLE"
    elif L[0] == 0 and L[1] == 0:
        return "IMPOSSIBLE"
    elif L[1] == 0 and L[2] == 0:
        return "IMPOSSIBLE"
    elif L[0] == 0 and L[2] == 0:
        return "IMPOSSIBLE"
    elif N > 1 and L[1] == 0 and L[0] == L[2]:
        return "IMPOSSIBLE"
    elif N > 1 and L[2] == 0 and L[0] == L[1]:
        return "IMPOSSIBLE"

    c = {0:'P', 1:'R', 2:'S'}

    for i in range(3):
        if L[i] > 0:
            choice = i
            result += c[i]
            L[i] -= 1
            break

    while sum(L) != 0:
        choice = (choice + 1) % 3
        while L[choice] == 0:
            choice = (choice + 1) % 3
        if L[choice] == 1 and L[(choice + 1) % 3] == 2 and L[(choice + 2) % 3] == 0:
            choice = (choice + 1) % 3
        result += c[choice]
        L[choice] -= 1

    return result

for test in range(1, input() + 1):
    N, R, P, S = [int(i) for i in raw_input().split()]
    N = int(N)
    R = int(R)
    P = int(P)
    S = int(S)
    L = [P, R, S]

    a = 'P' * P + 'R' * R + 'S' * S
    perms = [''.join(p) for p in itertools.permutations(a)]
    perms = set(perms)

    r = "Case #" + str(test) + ": "
    check = False
    for i in sorted(perms):
        if Check(i):
            check = True
            r += i
            break

    if check == False:
        r += "IMPOSSIBLE"

    print r
