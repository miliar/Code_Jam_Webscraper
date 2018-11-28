from Codejam import codejam_run, line as l

inf = float("inf")

def calc_time(sa, va, sb, vb):
    if vb >= va:
        return inf
    return (sb - sa) / (va - vb)


def update(t, s, v):
    return (s + v * t, v)

@codejam_run(l(D=int, N=int),\
             l(times="N", array_name="Horses"))
def solve(N, D, Horses):

    last_horse_t = 0

    Horses = [tuple(h) for h in Horses]
    Horses.append((D, 0))           # the ethernal horse

    while len(Horses) > 0:
        Horses.sort()

        pivot = Horses.pop(0)

        pivot_coll_time = min([calc_time(*pivot, *h) for h in Horses],\
                              default=inf)

        if pivot_coll_time == inf:
            break

        last_horse_t += pivot_coll_time

        Horses = [update(pivot_coll_time, *h) for h in Horses]

    return " " + str(D / last_horse_t)
