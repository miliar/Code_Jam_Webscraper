#!/usr/bin/env python

import sys


def read_line(file_path):
    return (line.strip("\n") for line in open(file_path, 'r').readlines() if line.strip())


def get_number(generator):
    return int(generator.next())


def get_case_line(generator):
    wood_weights = {}
    wood_number = get_number(generator)
    wood_weights.update({
    	"Naomi": sorted([float(nbr) for nbr in str(generator.next()).split(' ')], reverse=True),
    	"Kevin": sorted([float(nbr) for nbr in str(generator.next()).split(' ')], reverse=True)
    	})
    return wood_number, wood_weights


def compute_game_points(woods_player1, woods_player2, points=0):
	for w1 in woods_player1:
		# print woods_player2
		# print w1
		for w2 in woods_player2:
			if w1 > w2:
				points += 1
				woods_player2 = woods_player2[woods_player2.index(w2)+1:]
				break
		if not woods_player2:
			break
	return points


if __name__ == '__main__':
    file_content = read_line(sys.argv[1])
    test_case_number = get_number(file_content)
    current_case = 1

    while current_case <= test_case_number:
    	wood_number, wood_weights = get_case_line(file_content)
    	deceitful_points = compute_game_points(wood_weights['Naomi'], wood_weights['Kevin'])
    	war_points = wood_number - compute_game_points(wood_weights['Kevin'], wood_weights['Naomi'])
    	print("Case #{0}: {1} {2}".format(current_case, deceitful_points, war_points))
    	current_case += 1