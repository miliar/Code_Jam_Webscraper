from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        # toss out the N
        f.readline()
        naomi = [float(val) for val in f.readline().strip().split(" ")]
        ken = [float(val) for val in f.readline().strip().split(" ")]
        yield [naomi, ken]


def ken_move(naomi_choice, ken_blocks):
    bigger_blocks = [block for block in ken_blocks if block > naomi_choice]
    if len(bigger_blocks) > 0:
        return min(bigger_blocks)
    else:
        return min(ken_blocks)


def naomi_war_move(naomi_blocks, ken_blocks=None):
    naomi_choice = max(naomi_blocks)
    naomi_tell = naomi_choice
    return (naomi_choice, naomi_tell)


def naomi_deceitful_war_move(naomi_blocks, ken_blocks=None):
    if len(naomi_blocks) == 1:
        naomi_choice = naomi_blocks[0]
        naomi_tell = naomi_choice
    else:
        ken_max = max(ken_blocks)
        # tell ken a number larger than his largest block to make him pick
        # his smallest block
        # choose the smallest block that covers his smallest block
        ken_min = min(ken_blocks)
        naomi_covers = [block for block in naomi_blocks if block > ken_min]
        if naomi_covers:
            naomi_choice = min(naomi_covers)
            naomi_tell = ken_max + 0.000001
        # if none of them cover, choose the smallest block and tell him
        # something between his largest and next-largest block to make him
        # use his largest block
        else:
            naomi_choice = min(naomi_blocks)
            naomi_tell = (ken_blocks[-1] + ken_blocks[-2]) / 2

    return naomi_choice, naomi_tell


def play(move_naomi, naomi_blocks, move_ken, ken_blocks):
    naomi_score = 0

    while naomi_blocks:
        naomi_choice, naomi_tell = move_naomi(naomi_blocks, ken_blocks)
        ken_choice = move_ken(naomi_tell, ken_blocks)
        naomi_blocks.remove(naomi_choice)
        ken_blocks.remove(ken_choice)
        if naomi_choice > ken_choice:
            naomi_score += 1
    return naomi_score


def check_case(case):
    naomi_blocks, ken_blocks = case

    deceitful = play(naomi_deceitful_war_move, list(naomi_blocks),
                     ken_move, list(ken_blocks))
    war = play(naomi_war_move, list(naomi_blocks),
               ken_move, list(ken_blocks))

    return [str(deceitful), str(war)]

if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + " ".join(check_case(case)))
