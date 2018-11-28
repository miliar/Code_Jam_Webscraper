#!/usr/bin/python3


def best_weight_K_war(opts):
    sK = opts['sK']
    n = opts['bN']
    for wK in sK:
        if wK > n:
            sK.remove(wK)
            return wK
    wK = sK[-1]
    sK.remove(wK)
    return wK


def best_weight_N_war(opts):
    sN = opts['sN']
    wN = sN[0]
    sN.remove(wN)
    return wN


def best_weight_K_Dwar(opts):
    sK = opts['sK']
    n = opts['bN']
    for wK in sK:
        if wK > n:
            sK.remove(wK)
            return wK
    wK = sK[-1]
    sK.remove(wK)
    return wK


def best_weight_N_Dwar(opts):
    sN = opts['sN']
    sK = opts['sK']

    trade_least = []
    from decimal import Decimal
    from decimal import setcontext
    from decimal import Context
    setcontext(Context(prec=10))
    items_left = len(sN)

    if items_left == 1:
        bN = sN[0]
        sN.remove(bN)
        return bN

    if sN[0] < sK[0] or sN[-1] < sK[-1]:
        tN = (sK[items_left-1] + sK[items_left-2]) / Decimal(2.0)
        bN = sN[0]
        sN.remove(bN)
        return tN
    else:

        bN = sN[items_left - 1]
        sN.remove(bN)
        return bN





def play_dwar(no_of_weights, N, K):
    pn = 0
    pk = 0
    from copy import deepcopy

    sN = list(deepcopy(N))
    sK = list(deepcopy(K))

    sN.sort()
    sK.sort()

    while no_of_weights != 0:
        bN = best_weight_N_Dwar({'sN': sN, 'sK': sK})
        bK = best_weight_K_Dwar({'bN': bN, 'sK': sK})
        
        if bK > bN:
            pk += 1
        else:
            pn += 1
        no_of_weights -= 1
    return pn


def play_war(no_of_weights, N, K):
    pn = 0
    pk = 0
    from copy import deepcopy

    sN = list(deepcopy(N))
    sK = list(deepcopy(K))

    sN.sort()
    sK.sort()

    while no_of_weights != 0:
        bN = best_weight_N_war({'sN': sN})
        bK = best_weight_K_war({'bN': bN, 'sK': sK})

        if bK > bN:
            pk += 1
        else:
            pn += 1
        no_of_weights -= 1
    return pn


def give_nextline(filename):
    with open(filename) as in_file:
        for line in in_file:
            if line is not None:
                yield line
            else:
                yield None


def run_tests(filename):
    nextline = give_nextline(filename)
    TESTS = int(next(nextline))
    from decimal import Decimal
    from decimal import setcontext
    from decimal import Context

    setcontext(Context(prec=10))

    for it in range(1, TESTS + 1):
        no_of_weights = int(next(nextline))

        N = map(Decimal, next(nextline).split(' '))
        K = map(Decimal, next(nextline).split(' '))

        print(
            'Case #' + str(it) + ': ' + str(play_dwar(no_of_weights, N, K)) + ' ' + str(play_war(no_of_weights, N, K)))

    return


def main():
    import sys

    tests_file = sys.argv[1] if len(sys.argv) > 1 else "input.data"

    run_tests(tests_file)


main()

