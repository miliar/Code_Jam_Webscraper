#!/usr/bin/env python3
import sys
import numpy as np

def play(n, k):
    d = 0
    w = 0

    # The rest of War without cheating
    nu = sorted(n)
    ku = sorted(k)
    for chosen_n in nu:
        j = np.searchsorted(ku,[chosen_n,],side='right')[0]
        if j < len(ku):
            chosen_k = ku.pop(j)
        else:
            chosen_k = ku.pop(0)

        if chosen_n > chosen_k:
            w += 1

    # let's cheat!
    ku = sorted(k)
    tu = []
    for chosen_k in ku:
        j = np.searchsorted(nu,[chosen_k,],side='right')[0]
        if j < len(nu):
            tu.append(nu.pop(j))
            d+= 1

    return d, w

def main(argv):
    if len(argv) != 2:
        print("Usage : {} input".format(argv[0]))
        return -1

    with open(argv[1]) as infile:
        nb_tests = int(infile.readline())

        #lets read the input!
        for t in range(nb_tests):
            n = int(infile.readline())
            naomi = [float(e) for e in infile.readline().split()]
            ken = [float(e) for e in infile.readline().split()]
            y, z = play(naomi, ken)
            print("Case #{}: {} {}".format(t+1, y, z))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
