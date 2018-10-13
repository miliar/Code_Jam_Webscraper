t = int(input())

IMPOSSIBLE = 2
IN_PROG = 1
DONE = 0

for case in range(1, t+1):
    Hd, Ad, Hk, Ak, B, D = [int(x) for x in input().split(' ')]
    Hd_o = Hd
    M=dict()
    def opt(Hd, Ad, Hk, Ak):
        if Hk <= 0:
            return DONE, 0, 0
        Hd -= Ak # Subtract here for when we do zero checking
        if Hd <= 0:
            return IMPOSSIBLE, 0, 0
        if (Hd, Ad, Hk, Ak) in M:
            rval = M[(Hd, Ad, Hk, Ak)]
            if rval[0] == IN_PROG:
                return IMPOSSIBLE, 0, 0
        else: # Calculate
            M[(Hd, Ad, Hk, Ak)] = (IN_PROG, 0, 0)
            heal = opt(Hd_o, Ad, Hk, Ak)
            attack = opt(Hd, Ad, Hk - Ad, Ak)
            if Ad < Hk:
                buff = opt(Hd, Ad + B, Hk, Ak)
            else:
                buff = (IMPOSSIBLE, 0, 0)
            if Ak > 0:
                debuff = opt(Hd, Ad, Hk, max(Ak - D, 0))
            else:
                debuff = (IMPOSSIBLE, 0, 0)
            res = [i for i in [heal, attack, buff, debuff] if i[0] == DONE]
            if len(res) > 0:
                res = min(res, key=lambda x: x[1])
                res = (res[0], res[1] + 1, res[2])
            else:
                res = (IMPOSSIBLE, 0, 0)
            M[(Hd, Ad, Hk, Ak)] = res
        return M[(Hd, Ad, Hk, Ak)]
    res = opt(Hd+Ak, Ad, Hk, Ak)
    if res[0] == DONE:
        res = res[1]
    else:
        res = "IMPOSSIBLE"
    print("Case #{}: {}".format(case, res))