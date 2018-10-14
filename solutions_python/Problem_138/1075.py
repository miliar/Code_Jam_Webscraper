"""
Jonathan Simowitz

Google Code Jam 2014
Qualification Round
"""

import bisect
import os


def find_gt(a, x):
    """
    Index of the leftmost value greater than X
    """
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return i
    raise ValueError


def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "D-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    num_test_cases = int(rf.readline().strip())
    for test_num in range(1, num_test_cases + 1):
        _ = rf.readline()  # num blocks
        naomi = [float(val) for val in rf.readline().strip().split(' ')]
        ken = [float(val) for val in rf.readline().strip().split(' ')]
        naomi.sort()
        ken.sort()
        # play War
        # Ken's strategy: If he can win, choose the smallest block larger
        # than Naomi's, otherwise choose the smallest block.
        #
        # Naomi's strategy: smallest to largest block.
        war_naomi_points = 0
        ken_war = ken[:]
        for naomi_choice in naomi:
            try:
                ken_choice_idx = find_gt(ken_war, naomi_choice)
                ken_war.pop(ken_choice_idx)
            except ValueError:
                ken_war.pop(0)
                war_naomi_points += 1
        # play Deceitful War by turning the previous strategy on its head
        dw_naomi_points = 0
        for ken_choice in ken:
            try:
                naomi_choice_idx = find_gt(naomi, ken_choice)
                naomi.pop(naomi_choice_idx)
                dw_naomi_points += 1
            except ValueError:
                # Naomi cannot score any more points
                break
        wf.write('Case #%s: %s %s\n' % (
            test_num, dw_naomi_points, war_naomi_points))
    rf.close()
    wf.close()


main()
