#!/usr/bin/env python

import os, sys
import codejam

def magicka(testcase):
    if len(testcase) != 1:
        raise RuntimeError, "Oops, we got a bad testcase!"
    test_data = testcase[0].split(" ")
    num_combs = int(test_data.pop(0))
    combs = {}
    for i in range(num_combs):
        comb = test_data.pop(0)
        if len(comb) != 3:
            raise RuntimeError, "Oops, we got a combination of %s, the wrong length!" % comb
        combs[frozenset([comb[0], comb[1]])] = comb[2]
    num_opposeds = int(test_data.pop(0))
    opposeds = {}
    for i in range(num_opposeds):
        opp = test_data.pop(0)
        if len(opp) != 2:
            raise RuntimeError, "Oops, we got an opposed of %s, the wrong length!" % opp
        if opp[0] not in opposeds:
            opposeds[opp[0]] = set()
        if opp[1] not in opposeds:
            opposeds[opp[1]] = set()
        opposeds[opp[0]].add(opp[1])
        opposeds[opp[1]].add(opp[0])
    len_incantation = int(test_data.pop(0))
    incantation = test_data.pop(0).strip()
    if len(incantation) != len_incantation:
        raise RuntimeError, "Oops, we got %d bases when we were told %d" % (len(incantation), len_incantation)

    #print "Combs are %s, opps are %s, incantation is %s" % (repr(combs), repr(opposeds), repr(incantation))

    # OK, let's process the incantation.
    final_incantation = []
    for base in incantation:
        changes_made = True
        final_incantation.append(base)
        while changes_made:
            #print "Incantation now %s" % repr(final_incantation)
            changes_made = False
            # First see if we should combine the last two.
            if len(final_incantation) >= 2:
                comb_index = frozenset([final_incantation[-2], final_incantation[-1]])
                if comb_index in combs:
                    final_incantation = final_incantation[:-2]
                    final_incantation.append(combs[comb_index])
                    #print "Combined bases, now %s" % repr(final_incantation)
                    changes_made = True
            # OK, now see if we should blow up the list.
            if len(final_incantation) >= 1 and final_incantation[-1] in opposeds:
                for i in opposeds[final_incantation[-1]]:
                    if i in final_incantation:
                        #print "Found opposites %s and %s, blowing up the list" % (final_incantation[-1], i)
                        final_incantation = []
                        changes_made = True

    return "[%s]" % ", ".join(final_incantation)

if __name__ == "__main__":
    codejam.main(sys.argv[1:], magicka, 1)
