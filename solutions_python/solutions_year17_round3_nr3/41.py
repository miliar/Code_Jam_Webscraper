from math import ceil, floor, pi
import numpy as np


# def estimate_proba(p):


def easy_ai(N, K, U, probas):
    for i, p in enumerate(1*probas):
        if i == 0:
            continue

        available = U + probas[:i].sum()
        if available >= i*p:
            U = available - i*p
            probas[:i] = p
        else:
            probas[:i] = available / i
            break
    else:
        i = N
        p = 1.
        available = U + probas[:i].sum()
        if available >= i * p:
            probas[:i] = p
        else:
            probas[:i] = available / i

    return probas.prod()


if __name__=='__main__':
    PATH_IN = 'C-small-1-attempt0.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()
        N = int(line[0])
        K = int(line[1])
        U = float(f_in.readline().strip())
        print(N, K, U)

        probas = [float(p) for p in f_in.readline().split()]
        probas = sorted(probas)
        probas = np.array(probas)
        print(probas)


        res = '%.9f' % easy_ai(N, K, U, probas)

        print('Case #%i: %s' % (t+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (t+1, res))
