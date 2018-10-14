from bisect import bisect_right

__author__ = 'tobias'
filename = 'D-large'


def optimal_counter(my_weights, told):
    weight_index = bisect_right(my_weights, told)
    if weight_index != len(my_weights):
        return my_weights.pop(weight_index)
    else:
        return my_weights.pop(0)


def play_normal(naomi_weights, ken_weights):
    points = 0
    for weight in naomi_weights:
        told = weight
        if told > optimal_counter(ken_weights, told):
            points += 1
    return points


def play_deceitful(naomi_weights, ken_weights):
    points = 0
    while (len(naomi_weights) > 0):
        told = naomi_weights[-1]
        i = bisect_right(ken_weights, told)
        if i == len(ken_weights):
            points += 1
            naomi_weights.pop()
            ken_weights.pop()
        else:
            naomi_weights.pop(0)
            ken_weights.pop()
    return points


with open('%s.in' % filename) as inp:
    with open('%s.out' % filename, 'w') as out:
        cases = inp.readline().strip()
        for case in range(int(cases)):
            num_weights = int(inp.readline().strip())
            naomi_weights = sorted([float(weight) for weight in inp.readline().strip().split()])
            ken_weights = sorted([float(weight) for weight in inp.readline().strip().split()])
            dec = play_deceitful(naomi_weights[:], ken_weights[:])
            war = play_normal(naomi_weights[:], ken_weights[:])
            output = '{} {}'.format(dec, war)
            out.write("Case #{case}: {out}\n".format(case=case + 1, out=output))