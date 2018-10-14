from __future__ import print_function
from decimal import Decimal
from bisect import bisect_left
import random

INPUT = "D-large.bin"
OUTPUT = "D-large.out"


def ken_best(Ken, naomi_element):
    return bisect_left(Ken, naomi_element) % len(Ken)


def war(Naomi, Ken):
    naomi_wins = 0
    while Naomi:
        chosen_naomi = Naomi.pop(random.randint(0, len(Naomi) - 1))
        chosen_ken = Ken.pop(ken_best(Ken, chosen_naomi))
        # print("%r %r" % (chosen_naomi, chosen_ken))
        if chosen_naomi > chosen_ken:
            naomi_wins += 1
    return naomi_wins


def deceitfulWar(Naomi, Ken):
    i = 0
    while i < len(Naomi):
        if Naomi[i] < Ken[i]:
            naomi_chosen = Naomi.pop(i)
            if len(Ken) < 2:
                naomi_told = Ken[-1] - 1
            else:
                naomi_told = Ken[-2] + ((Ken[-1] - Ken[-2]) / 2)
            ken_chosen = Ken.pop(ken_best(Ken, naomi_told))
        else:
            i += 1

    return len(Naomi)


def round(number, fp):
    fp.readline()
    Naomi = sorted([Decimal(x) for x in fp.readline().split(' ')])
    Ken = sorted([Decimal(x) for x in fp.readline().split(' ')])

    return "%d %d" % (deceitfulWar(Naomi[:], Ken[:]), war(Naomi[:], Ken[:]))


def solver(filename):
    with open(filename, 'r') as fp:
        cases = int(fp.readline())
        for case in range(cases):
            result = round(case + 1, fp)
            yield case + 1, result

if __name__ == "__main__":
    with open(OUTPUT, "wt") as fp:
        for result in solver(INPUT):
            fp.write("Case #%d: %s\n" % (result))
    print("DONE")
