#! /usr/bin/env python

import sys

def simulate_optimal_war(player1_blocks, player2_blocks, blocks):
    points_player1 = 0
    points_player2 = 0
    player1_blocks = player1_blocks[:]
    player2_blocks = player2_blocks[:]
    for i in range(0, blocks):
        player1_choice = _player1_optimal_choice_war(player1_blocks)
        player2_choice = _player2_optimal_choice_war(player2_blocks,
                player1_choice)
        player1_blocks.remove(player1_choice)
        player2_blocks.remove(player2_choice)
        if player1_choice > player2_choice:
            points_player1 += 1
        else:
            points_player2 += 1
    return points_player1

def _player1_optimal_choice_war(player1_blocks):
    return max(player1_blocks)

def _player1_optimal_deceitful_war(player1_blocks, player2_blocks):
    player1_told_choice  = 0
    player1_max = max(player1_blocks)
    player1_min = min(player1_blocks)
    player2_max = max(player2_blocks)
    player2_min = min(player2_blocks)

    if player2_max > player1_max:
        # Choose the minimal but tell a lie.
        player1_choice = min(player1_blocks)
        player1_told_choice = player2_max - 0.00000001
    else:
        item = None
        minimal_greater = 1
        for i in player1_blocks:
            distance = i - player2_min
            if i >  player2_min and distance <= minimal_greater:
                minimal_greater = distance
                item = i
        player1_choice = item
        player1_told_choice = player2_max + 0.00000001


    return player1_choice, player1_told_choice

def _player2_optimal_choice_war(player2_blocks, player1_choice):
    item = None
    minimal_greater = 1
    for i in player2_blocks:
        distance = i - player1_choice
        if i > player1_choice and distance <= minimal_greater:
            minimal_greater = distance
            item = i

    item = min(player2_blocks) if item is None else item
    return item

def simulate_optimal_deceitful_war(player1_blocks, player2_blocks, blocks):
    points_player1 = 0
    points_player2 = 0
    for i in range(0, blocks):
        player1_choice, player1_told_choice = _player1_optimal_deceitful_war(player1_blocks,
                player2_blocks)
        player2_choice = _player2_optimal_choice_war(player2_blocks,
                player1_told_choice)
        player1_blocks.remove(player1_choice)
        player2_blocks.remove(player2_choice)
        if player1_choice > player2_choice:
            points_player1 += 1
        else:
            points_player2 += 1
    return points_player1

def solve_problem(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'w+')
    test_cases = int(input_file.readline())
    for i in range(0, test_cases):
        blocks = int(input_file.readline())
        line_player1_blocks = input_file.readline().split()
        line_player2_blocks = input_file.readline().split()

        player1_blocks = [float(x) for x in line_player1_blocks]
        player2_blocks = [float(x) for x in line_player2_blocks]

        points_war = simulate_optimal_war(player1_blocks,
                player2_blocks, blocks)
        points_deceitful_war = simulate_optimal_deceitful_war(player1_blocks,
                player2_blocks, blocks)

        line = "Case #{}: {} {}".format(i+1, points_deceitful_war, points_war)
        output_file.write(line + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Missing intput/output files')
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    solve_problem(input_file, output_file)

