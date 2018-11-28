#!/usr/bin/python

import sys

def match_1(match1, match2, candidate1, candidate2):
    if match1 == candidate1 and match2 == candidate2 or match1 == candidate2 and match2 == candidate1:
        return True

def combine(combinations, candidates):
    for combination in combinations:
        if match_1(combination[0], combination[1], queue[-1], queue[-2]):
            del queue[-2:]
            queue.append(combination[2])
            return candidates
    return candidates

def collide(oppositions, candidates):
    for opposition in oppositions:
        if opposition[0] in candidates and opposition[1] in candidates:
            return []
    return candidates

# Read in input
num_problems = int(sys.stdin.readline())

for problem_number in range(1, num_problems + 1):
    tokens = sys.stdin.readline().split(' ')
    num_combinations = int(tokens.pop(0))
    combinations = []
    for idx in range(num_combinations):
        combinations.append(tokens.pop(0))
    num_oppositions = int(tokens.pop(0))
    oppositions = []
    for idx in range(num_oppositions):
        oppositions.append(tokens.pop(0))
    num_characters = int(tokens.pop(0))
    string = tokens[0][:num_characters]

    queue = []
    for character in string:
        queue.append(character)
        if len(queue) > 1:
            queue = combine(combinations, queue)
        if len(queue) > 1:
            queue = collide(oppositions, queue)
    # Output template
    print "Case #" + str(problem_number) + ": [" + ", ".join(queue) + "]" 
