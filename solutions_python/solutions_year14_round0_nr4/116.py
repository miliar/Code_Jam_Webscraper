"""
Google Code Jam 2014 Qualification Problem D
Usage:
    python d.py < input.txt > output.txt
"""
import sys


def play_dwar(naomi_blocks, ken_blocks):
    max_score = 0

    while naomi_blocks:
        if min(naomi_blocks) > min(ken_blocks):
            max_score += 1
            naomi_blocks = naomi_blocks[1:]
            ken_blocks = ken_blocks[1:]
        else:
            naomi_blocks = naomi_blocks[1:]
            ken_blocks = ken_blocks[:-1]

    return max_score


def play_war(naomi_blocks, ken_blocks):
    max_score = 0
    while naomi_blocks:
        if max(naomi_blocks) > max(ken_blocks):
            max_score += 1
            naomi_blocks = naomi_blocks[:-1]
            ken_blocks = ken_blocks[1:]
        else:
            naomi_blocks = naomi_blocks[:-1]
            ken_blocks = ken_blocks[:-1]

    return max_score


def solve_problem(naomi_blocks, ken_blocks):
    return play_dwar(naomi_blocks, ken_blocks), play_war(naomi_blocks, ken_blocks)


if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())
    for i in xrange(1, num_of_cases + 1):

        num_of_blocks = int(sys.stdin.readline().strip())

        naomi_blocks = sorted(map(float, sys.stdin.readline().strip().split()))
        ken_blocks = sorted(map(float, sys.stdin.readline().strip().split()))


        print "Case #{0}: {1} {2}".format(i, *solve_problem(naomi_blocks, ken_blocks))
