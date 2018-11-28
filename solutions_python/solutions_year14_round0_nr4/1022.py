import bisect

tcnum = int(input())


def ken(blocks, weight_naomi):
    if weight_naomi > blocks[-1]:
        return blocks.pop(0)
    return blocks.pop(bisect.bisect(blocks, weight_naomi))


def naomi(blocks, _):
    w = blocks.pop(0)
    return w, w


def naomi_deceitful(blocks_naomi, blocks_ken):
    b = blocks_naomi.pop(0)
    if b > blocks_ken[0]:
        return b, blocks_ken[-1] + 1
    return b, blocks_ken[-1] - 0.00000001


def run_game(naomi, ken, blocks_naomi, blocks_ken):
    blocks_naomi = blocks_naomi[:]
    blocks_ken = blocks_ken[:]
    naomi_won = 0
    while len(blocks_ken) > 0:
        naomi_real, naomi_deceit = naomi(blocks_naomi, blocks_ken)
        ken_real = ken(blocks_ken, naomi_deceit)
        if (naomi_real > ken_real) != (naomi_deceit > ken_real):
            print("Ken discovered Naomi's trickery!")
            return 0
        if naomi_deceit > ken_real:
            naomi_won += 1
    return naomi_won


for tc in range(tcnum):
    input()
    blocks_naomi = sorted([float(w) for w in input().split()])
    blocks_ken = sorted([float(w) for w in input().split()])
    win_deceitful = run_game(naomi_deceitful, ken, blocks_naomi, blocks_ken)
    win_real = run_game(naomi, ken, blocks_naomi, blocks_ken)
    print("Case #{}: {} {}".format(tc + 1, win_deceitful, win_real))
