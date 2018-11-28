def f(p):
    s1, t1 = p[0]
    s2, t2 = p[1]
    x = g(s1, t1, s2, t2)
    if x:
        return 2
    else:
        return 4

def g(s1, t1, s2, t2):
    if (t2 - s1) <= 12 * 60:
        return True
    if (s2 - t1) >= 12 * 60:
        return True
    return False

T = int(input())
for tid in range(T):
    C, J = [int(x) for x in input().split(' ')]
    AC = []
    AJ = []
    for i in range(C):
        c, d = [int(x) for x in input().split(' ')]
        AC.append((c, d))
    for i in range(J):
        c, d = [int(x) for x in input().split(' ')]
        AJ.append((c, d))

    AC.sort()
    AJ.sort()
    if (C + J <= 1):
        result = 2
    if (C == 1) and (J == 1):
        result = 2
    else:
        if (C == 2):
            result = f(AC)
        elif (J == 2):
            result = f(AJ)



    print('Case #{}: {}'.format(tid + 1, str(result)))
