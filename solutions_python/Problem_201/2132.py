""" Bathroom Stall Recursion problem"""
from sys import stdin
def place_person(stall_layout):
    # First we need to find all the unoccupied subslices
    trailing_position = 0
    max_dist_best = 0
    min_dist_best = -1
    best_position = 0
    for i in range(1, len(stall_layout)):
        length = stall_layout[i] - stall_layout[i -1] - 1
        if length % 2 == 0:
            max_dist = length // 2
            min_dist = length // 2 - 1
            position = stall_layout[i - 1] + min_dist + 1
        else:
            max_dist = length // 2
            min_dist = length // 2
            position = stall_layout[i - 1] + min_dist + 1
        if min_dist_best < min_dist or (min_dist_best == min_dist and max_dist > max_dist_best):
            min_dist_best = min_dist
            best_position = position
            max_dist_best = max_dist

    stall_layout.append(best_position)
    stall_layout.sort()
    return max_dist_best, min_dist_best, stall_layout


def solve_stalls(stalls, people):
    stall_layout = [0, stalls+1]
    for i in range(people):
        max_dist, min_dist, stall_layout = place_person(stall_layout)
    return max_dist, min_dist


def main():
    test_cases  = int(stdin.readline())
    for i in range(1, test_cases + 1):
        stalls, people = (int(z) for z in stdin.readline().split())
        max_dist, min_dist = solve_stalls(stalls, people)
        print("Case #%s: %i %i" % (str(i), max_dist, min_dist))

main()
