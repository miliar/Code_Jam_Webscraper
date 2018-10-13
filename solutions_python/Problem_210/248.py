

def zeit(p, z):
    t = 0
    for i in range(len(z) - 1):
        if z[i][0] == p:
            t += z[i+1][1] - z[i][1]
    if z[-1][0] == p:
        t += (1440 - z[-1][1]) + z[0][1]
    return t

def spiel(p, z):
    """Finde slot in z mit maximalem Spiel fuer p.
    """
    max_i = -1
    max_s = 0
    for i in range(len(z) - 1):
        if z[i][0] != p and z[i][2] < z[i+1][1]:
            s = z[i+1][1] - z[i][2]
            if s > max_s:
                max_i = i
                max_s = s
    if z[-1][0] != p:
        s = 1440 - z[-1][2] + z[0][1]
        if s > max_s:
            max_i = len(z) - 1
            max_s = s
    return max_i, max_s

def ins(p, i, z, a):
    """Arbeit fuer p nach Position i einfuegen, Menge a."""
    if i < len(z) - 1:
        t = z[i+1][1] - a
        z.insert(i + 1, (p, t, t))
    elif z[0][1] >= a:
        t = z[0][1] - a
        z.insert(0, (p, t, t))
    else:
        t = 1440 - (a - z[0][1])
        assert t >= z[-1][2]
        z.append((p, t, t))

def flanken(z):
    s = 0
    prev = z[-1][0]
    for x in z:
        if prev != x[0]:
            s += 1
        prev = x[0]
    return s

def solve(cact, jact):
    if len(cact) + len(jact) == 1:
        return 2
    cact = sorted(cact)
    jact = sorted(jact)
    z = []
    while cact and jact:
        if cact[0] < jact[0]:
            z.append(('J', cact[0][0], cact[0][1]))
            del cact[0]
        else:
            z.append(('C', jact[0][0], jact[0][1]))
            del jact[0]
    if cact:
        z.extend(('J', x[0], x[1]) for x in cact)
    if jact:
        z.extend(('C', x[0], x[1]) for x in jact)
    #print(z)
    #print(zeit('C', z), zeit('J', z))
    tc = zeit('C', z)
    while tc != 720:
        p = 'C' if tc < 720 else 'J'
        i, s = spiel(p, z)
        assert s > 0
        a = min(s, abs(720 - tc))
        ins(p, i, z, a)
        tc = zeit('C', z)
        #print(z, tc)
    return flanken(z)

t = int(input())
for i in range(1, t + 1):
    ac, aj = [int(c) for c in input().split(" ")]
    cakes = []
    c_act = [tuple([int(c) for c in input().split(" ")]) for _ in range(ac)]
    j_act = [tuple([int(c) for c in input().split(" ")]) for _ in range(aj)]
    print("Case #{}: {}".format(i, solve(c_act, j_act)))
