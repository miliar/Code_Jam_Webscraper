# Small assignment 1: n = k
def core1(n, u, ps):
    sorted_ps = sorted(ps)
    optimal_ps = optimize1(sorted_ps, u, 1)
    comb_prob = combine_probs(optimal_ps)
    return comb_prob


# Divide the available U over the first nb_ps sorted ps
# Done by adding until either U runs out, or until the first
# nb_ps reach the next biggest p
def optimize1(s_ps, u, nb_ps):
    if nb_ps == len(s_ps):
        div_u = float(u) / nb_ps
        new_ps = [p + div_u for p in s_ps]
        return new_ps
    next_p = s_ps[nb_ps]
    rem_p = reduce(lambda acc, c_p: acc + (next_p - c_p), s_ps[:nb_ps], 0)
    if rem_p <= u:
        new_ps = [next_p for _ in range(nb_ps)] + s_ps[nb_ps:]
        return optimize1(new_ps, u-rem_p, nb_ps+1)
    target_p = (sum(s_ps[:nb_ps]) + u) / nb_ps
    opt_ps = [target_p for _ in range(nb_ps)] + s_ps[nb_ps:]
    return opt_ps


def combine_probs(ps):
    return reduce(lambda x, y: x*y, ps)


input_t = int(raw_input())
for i in xrange(1, input_t + 1):
    i_n, i_k = [int(st) for st in raw_input().split(" ")]
    i_u = float(raw_input())
    i_ps = [float(st) for st in raw_input().split(" ")]
    result = core1(i_n, i_u, i_ps)
    print "Case #{}: {}".format(i, result)
# print core1(4, 1.4, [0.5, 0.7, 0.8, 0.6])
