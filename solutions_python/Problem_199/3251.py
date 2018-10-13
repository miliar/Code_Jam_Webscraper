# Author: Hurturk Yagmur
# Codejam Qualification Round 2017 - Problem A - Oversized Pancake Flipper

import re

def print_case(n, result):
    print("Case #%d: %s" % ((n+1), str(result)))

def flip_portion(s, index, flipper_size):
    for i, c in enumerate(s[index:index+flipper_size]):
        if c == '-':
            s[index+i] = '+'
        else:
            s[index+i] = '-'

T = int(raw_input())

for case in range(0, T):
    current = raw_input().split(" ")
    pancakes = list(current[0])
    flipper_size = int(current[1])
    
    #if all is + -> 0
    all_is_happy = re.compile("^[\+]+$")
    if len(pancakes) == 0 or all_is_happy.match(''.join(pancakes)):
        print_case(case, 0)
        continue

    #if flipper_size == 0 -> "IMPOSSIBLE" 
    if flipper_size == 0 or flipper_size > len(pancakes):
        print_case(case, "IMPOSSIBLE")
        continue

    beginning = 0
    ending = len(pancakes)
    moves = 0
    while (ending - beginning) >= flipper_size and not all_is_happy.match(''.join(pancakes[beginning:ending])):
        #beginning match check, flip from beginning
        if pancakes[beginning] == '-':
            flip_portion(pancakes, beginning, flipper_size)
            moves += 1

        #ending match check, flip from end
        if pancakes[ending-1] == '-':
            flip_portion(pancakes, ending - flipper_size, flipper_size)
            moves += 1

        #narrow down until one and try again
        beginning = ''.join(pancakes).find("-")
        ending = ''.join(pancakes).rfind("-") + 1

    if all_is_happy.match(''.join(pancakes)):
        print_case(case, moves)
    else:
        print_case(case, "IMPOSSIBLE")

