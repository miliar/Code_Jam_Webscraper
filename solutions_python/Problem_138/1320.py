#!/usr/bin/env python

"""
Google Code Jam 2014
Qualification round
Problem D. Deceitful War

Thinking:
In Deceiptful War, if Naomi has a block that is so light it cannot beat any of Ken's blocks,
the best use for that block is to trick him into playing his best block. That means Naomi's
worst blocks "cancel out" Ken's best blocks. All the other blocks, Naomi can win on.

So Naomi's losses will be the maximum of (the count of Naomi's blocks which cannot beat any of Ken's blocks, and
                                          the count of Ken's blocks which beat every one of Naomi's blocks)

Obviously, Naomi's wins, the number the program is to report, will be the number of rounds minus her losses.

Update:
Imagine this crafted input:
4
0.2 0.3 0.4 0.7
0.1 0.5 0.6 0.8

Naomi can win, I think at most, 2 points.

Game log:
Naomi plays 0.2 to beat Ken's 0.1
Noami plays 0.3 to get rid of Ken's 0.8
Noami plays 0.7 to beat Ken's 0.6
But now Naomi is left with 0.4 and Ken has a 0.5.

Basically Naomi's 0.2, 0.3, and 0.4 blocks can only be used to beat Ken's 0.1 block or get rid of his 0.8 block. That's
 3 blocks used against 2. So one of them is going to go to waste.

The problem with my approach above is it only looks at the outer ends of the block list. It needs to look inside the list
for situations like this. I think the easiest way is to just program Naomi's strategy and have the program play for real.


"""

import sys
import argparse
import random

naomi = ken = []

class TestCase:
    pass

def naomi_pick():
    return naomi.pop(random.randint(0, len(naomi) - 1))

def naomi_pick_deceit():
    global naomi
    global ken

    MARGIN = 0.000001

    # get rid of unbeatable blocks

    if (ken[-1] > naomi[-1]):
        return (naomi.pop(0), ken[-1] - MARGIN)

    # score a point if possible, beating ken by the slimmest margin
    for (i, block) in enumerate(naomi):
        if block > ken[0]:
            return (naomi.pop(i), ken[-1] + MARGIN) # ken will play his worst block, ken[0]

    # otherwise doesn't matter, return any block, going to lose
    np = naomi.pop[0]
    return (np, np)

def ken_pick(np):
    diffs = [k - np for k in ken]
    if diffs[-1] > 0: # Ken can win
        for (i, v) in enumerate(diffs):
            if v > 0:
                return ken.pop(i) # return the block that wins by the smallest margin
    else: # return the worst block
        return ken.pop(0)


def process_input(args):
    casescount = int(args.filename.readline())
    testcases = []

    for i in range(casescount):
        args.filename.readline() # throw away block count

        testcase = TestCase()
        testcase.N = args.filename.readline()
        testcase.K = args.filename.readline()
        testcases.append(testcase)

    args.filename.close()

    return testcases

def process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=argparse.FileType('r'),
                        help="Input file")
    args = parser.parse_args()

    return args

def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for (i, case) in enumerate(testcases):
        global naomi
        naomi = case.N.split()
        global ken
        ken = case.K.split()
        naomi = map(float, naomi)
        naomi.sort()
        ken = map(float, ken)
        ken.sort()

        # naomis_worthless_blocks = 0
        # while  naomis_worthless_blocks < len(naomi) and naomi[naomis_worthless_blocks] < ken[0]: # first criteria handles all worthless blocks
        #     naomis_worthless_blocks += 1
        #
        # kens_unbeatable_blocks = len(ken) - 1
        # while  kens_unbeatable_blocks >= 0 and naomi[-1] < ken[kens_unbeatable_blocks]:
        #     kens_unbeatable_blocks -= 1
        #
        # kens_unbeatable_blocks = len(ken) - 1 - kens_unbeatable_blocks
        #
        # # debug print "Naomi has " + str(naomis_worthless_blocks) + " worthless blocks, Ken has " + str(kens_unbeatable_blocks) + " unbeatable)"
        #
        # naomi_forced_losses = max(naomis_worthless_blocks, kens_unbeatable_blocks)
        # naomi_deceipt_wins = len(naomi) - naomi_forced_losses

        picks = []
        while len(naomi) > 0:
            np = naomi_pick()
            picks.append((np, ken_pick(np)))

        outcomes = [n > k for (n, k) in picks]

        # Reset for Deceitful War
        naomi = case.N.split()
        ken = case.K.split()
        naomi = map(float, naomi)
        naomi.sort()
        ken = map(float, ken)
        ken.sort()

        picks_deceit = []
        while len(naomi) > 0:
            np, npt = naomi_pick_deceit()
            picks_deceit.append((np, ken_pick(npt)))

        outcomes_deceit = [n > k for (n, k) in picks_deceit]

        print "Case #" + str(i + 1) + ": " + str(outcomes_deceit.count(True)) + " " + str(outcomes.count(True))
        # debug print "War " + str(i) + ": Naomi won " + str(outcomes.count(True)) + " times. " # + " Picks:" + str(picks)
        # debug print "Deceitful War " + str(i) + ": Naomi won " + str(naomi_deceipt_wins) + " times"

    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
