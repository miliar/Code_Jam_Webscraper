# Debuffs, then buffs, then attacks/heals

def debuffs(hd, ak, d):
    yield (hd, ak, 0)
    if d == 0:
        return

    hd_curr = hd
    ak_curr = ak
    turns = 0
    last_move = None

    while ak_curr > 0:
        turns += 1
        if hd_curr - (ak_curr-d) <= 0:
            if last_move == 'h':
                return

            # Heal
            hd_curr = hd - ak_curr
            last_move = 'h'
        else:
            ak_curr -= d
            ak_curr = max(0, ak_curr)
            hd_curr -= ak_curr

            yield (hd_curr, ak_curr, turns)
            last_move = 'd'


def buffs(hd, hd_curr, ad, hk, ak_curr, b, turns):
    yield (hd_curr, ad, turns)
    if b == 0:
        return

    ad_curr = ad
    last_move = None
    
    while ad_curr < hk:
        turns += 1
        if hd_curr - ak_curr <= 0:
            if last_move == 'h':
                return

            # Heal
            hd_curr = hd - ak_curr
            last_move = 'h'
        else:
            ad_curr += b
            hd_curr -= ak_curr

            yield(hd_curr, ad_curr, turns)
            last_move = 'b'


def solve(hd, ad, hk, ak, b, d):
    m = None

    for hd_curr, ak_curr, turns in debuffs(hd, ak, d):
        # print("D", hd_curr, ak_curr, turns)
        for hd_curr2, ad_curr, turns2 in buffs(hd, hd_curr, ad, hk, ak_curr, b, turns):
            # print("   ", hd_curr, ad_curr, hk, ak_curr, turns2)
            
            # Attack/heal from now on.
            hk_curr = hk
            last_move = None

            while hk_curr > 0:
                turns2 += 1
                if hd_curr2 - ak_curr <= 0 and ad_curr < hk_curr:
                    if last_move == 'h':
                        break

                    # Heal
                    hd_curr2 = hd - ak_curr
                    last_move = 'h'
                else:
                    hk_curr -= ad_curr
                    hd_curr2 -= ak_curr
                    last_move = 'a'

            else:
                if m is None:
                    m = turns2
                else:
                    m = min(m, turns2)

    return m


with open('C-small-attempt0.in') as infile:
    with open('C-small-attempt0.out', 'w') as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):
            hd, ad, hk, ak, b, d = map(int, next(infile).split())
            r = solve(hd, ad, hk, ak, b, d)

            if r is None:
                r = "IMPOSSIBLE"

            print("Case #{}: {}".format(case, r), file=outfile)
            print(case, r)
