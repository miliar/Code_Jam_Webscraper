from decimal import Decimal as D
from copy import copy
import bisect

filename = 'D-large'
inputfile = filename + '.in'
outputfile = filename + '.out'

def play_optimal(weight, my_weights):
    return bisect.bisect_left(my_weights, weight)


def war(naomis, kens):
    naomis_point = 0
    kens_point = 0
    for naomi in naomis:
        i = play_optimal(naomi, kens)
        if i >= len(kens):
            i = len(kens) - 1
        if naomi > kens.pop(i):
            naomis_point += 1
        else:
            kens_point += 1
    assert l == naomis_point + kens_point
    return naomis_point

def deceitful_war(naomis, kens):
    naomis_point = 0
    kens_point = 0
    for naomi in naomis:
        if naomi > kens[-1]:
            i = play_optimal(naomi, kens)
            if i >= len(kens):
                i = len(kens) - 1
            k = kens.pop(i)
            if naomi > k:
                naomis_point += 1
            else:
                kens_point += 1
        elif naomi > kens[0]:
            i = play_optimal(kens[-1] + D("0.0000000001"), kens)
            i = 0
            k = kens.pop(i)
            if naomi > k:
                assert True, (naomi, k)
                naomis_point += 1
            else:
                assert False, (naomi, k)
                kens_point += 1
        else:
            i = play_optimal(kens[-1] - D("0.0000000001"), kens)
            if i >= len(kens):
                i = len(kens) - 1
            k = kens.pop(i)
            if naomi > k:
                assert False
                naomis_point += 1
            else:
                assert True
                kens_point += 1
    assert l == naomis_point + kens_point
    return naomis_point

with open(inputfile) as input, open(outputfile, 'w') as output:
    T = int(input.readline())
    for t in xrange(T):
        l = int(input.readline())
        naomis = sorted(map(D, input.readline().split()))
        kens = sorted(map(D, input.readline().split()))
        output.write("Case #{t}: {y} {z}\n".format(t=t+1, y=deceitful_war(copy(naomis), copy(kens)), z=war(copy(naomis), copy(kens))))
