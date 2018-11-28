

def gen_lrs(stalls):
    stall_out = [[0,0] for s in stalls]

    Rs = 0
    for i, x in enumerate(stalls):
        stall_out[i][0] = Rs

        if x == 1:
            Rs = 0
        else:
            Rs += 1

    stall_out.reverse()
    stalls.reverse()

    Ls = 0
    for i, x in enumerate(stalls):
        stall_out[i][1] = Ls

        if x == 1:
            Ls = 0
        else:
            Ls += 1

    stall_out.reverse()
    stalls.reverse()

    return stall_out

def get_best_spot(stalls, lrs):
    highscore = 0

    for i, lr in enumerate(lrs):
        if stalls[i] == 1:
            continue

        mx = min(lr[0], lr[1])
        if mx > highscore:
            highscore = mx

    best_stalls = []

    for i, lr in enumerate(lrs):
        if stalls[i] == 1:
            continue
        if min(lr[0], lr[1]) == highscore:
            best_stalls.append(i)

    if len(best_stalls) > 1:
        highscore_max = 0

        for i in best_stalls:
            if stalls[i] == 1:
                continue

            mx = max(lrs[i][0], lrs[i][1])
            if mx > highscore_max:
                highscore_max = mx

        best_stalls_max = []
        for i in best_stalls:
            if stalls[i] == 1:
                continue
            if max(lrs[i][0], lrs[i][1]) == highscore_max:
                best_stalls_max.append(i)

        if len(best_stalls_max) >= 1:
            return best_stalls_max[0]

    elif len(best_stalls) == 1:
        return best_stalls[0]

    print("ERROR! NOT ENOUGH STALLS")


t = int(input())
for i in range(1, t + 1):
    n, k = (input().split(' '))

    stalls = [1] + ([0] * int(n)) + [1]

    lrs = []
    for person in range(0, int(k)):
        lrs = gen_lrs(stalls)
        spot = get_best_spot(stalls, lrs)
        stalls[spot] = 1


    max_lrs = max(lrs[spot][0], lrs[spot][1])
    min_lrs = min(lrs[spot][0], lrs[spot][1])

    print("Case #{}: {} {}".format(i, max_lrs, min_lrs))
