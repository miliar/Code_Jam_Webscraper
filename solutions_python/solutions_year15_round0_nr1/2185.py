#!/usr/bin/env python
# -*- coding: utf-8 -*-

test_inputs = [
    (4, "11111"),
    (1, "09"),
    (5, "110011"),
    (0, "1"),
]

def bring_friends(s_max, start_index, shiny_guys, standing_up):
    "Return how many more guys are required"
    total = 0
    while True:
        if not shiny_guys:
            break
        if start_index >= len(shiny_guys):
            break
        if start_index > s_max:
            break
        current_shy = int(shiny_guys[start_index])
        if start_index and current_shy:
            required_shyness = start_index
            more_to_bring = 0
            if standing_up < required_shyness:
                more_to_bring += required_shyness - standing_up
            all_standing = standing_up + current_shy + more_to_bring
            # next
            start_index += 1
            total += more_to_bring
            standing_up = all_standing
        else:
            start_index += 1
            standing_up += current_shy
    return total

if __name__ == '__main__':
    for case_number in range(int(raw_input().strip())):
        s_max, shinies = raw_input().strip().split()
        s_max = int(s_max)
        print("Case #{}: {}".format(case_number+1, bring_friends(s_max, 0, shinies, 0)))

