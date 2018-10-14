#!/usr/bin/python
# -*- coding: utf-8 -*-


import random

SECOND_LARGEST = -2
LARGEST = -1
orig_naomi_wts = None
orig_ken_wts = None
MAX_WT = 0.9999999


def get_wt_greater_than(min_value, ken_wts, wts_told):
    # returns a value greater than ken_wts[min_value]
    wt = random.uniform(ken_wts[min_value], MAX_WT)
    while wt in wts_told:
        wt = random.uniform(ken_wts[min_value], MAX_WT)
    return wt


def deceitful_war(naomi_wts, ken_wts):
    wts_told = set()

    n_pts = 0       # Naomi's points

    while len(naomi_wts) > 0:
        n_wt = naomi_wts.pop(0)

        # print('n_wt > {}'.format(str(n_wt)))

        # in case this is the last weight
        if len(ken_wts) == 1:
            if n_wt > ken_wts.pop():
                n_pts += 1
            continue

        if n_wt < ken_wts[0]:
            # tell the weight to be greater than the second largest wt of ken
            n_tell = get_wt_greater_than(SECOND_LARGEST, ken_wts, wts_told)
            wts_told.add(n_tell)
            ken_wts.pop(-1)
        else:
            # since the lowest weight that naomi has is larger than the lowest
            # weight that ken has, bluff the wt to be larger than the largest
            # wt that ken has, so that he would throw the lowest wt and naomi
            # would win the pt
            n_tell = get_wt_greater_than(LARGEST, ken_wts, wts_told)
            wts_told.add(n_tell)
            ken_wts.pop(0)
            n_pts += 1

    return n_pts


def get_ken_wt(ken_wts, n_wt):
    # find the min wt in ken_wts that is greater than n_wt
    popup_index = None

    for i, wt in enumerate(ken_wts):
        if wt > n_wt:
            popup_index = i
            break

    if popup_index is None:
        return None
    else:
        return ken_wts.pop(popup_index)


def war(naomi_wts, ken_wts):
    n_pts = 0

    while len(ken_wts) > 0:
        n_wt = naomi_wts.pop(0)

        # ken finds the min wt he has which is greater than n_wt
        k_wt = get_ken_wt(ken_wts, n_wt)
        if k_wt is None:
            # ken does not have any more items which are greater than n_wt
            ken_wts.pop(0)
            n_pts += 1

    return n_pts


def solve(n, naomi_wts, ken_wts):
    # reverse sort the wts list
    naomi_wts = sorted(naomi_wts)
    ken_wts = sorted(ken_wts)

    # print('naomi_wts > {}'.format(naomi_wts))
    # print('ken_wts > {}'.format(ken_wts))

    global orig_naomi_wts, orig_ken_wts
    orig_naomi_wts = set(naomi_wts)
    orig_ken_wts = set(ken_wts)

    war_pts = war(naomi_wts[:], ken_wts[:])
    d_war_pts = deceitful_war(naomi_wts[:], ken_wts[:])

    return '{} {}'.format(str(d_war_pts), str(war_pts))


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        n = input()
        naomi_wts = [float(wt) for wt in raw_input().strip().split()]
        ken_wts = [float(wt) for wt in raw_input().strip().split()]

        print("Case #%i: %s" % (caseNr, solve(n, naomi_wts, ken_wts)))
