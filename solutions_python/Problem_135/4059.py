#!/usr/bin/env python3

get_possible = lambda row: set([input() for k in range(4)][row-1].split())

for i in range(int(input())):
    matches = get_possible(int(input())) & get_possible(int(input()))
    if not matches: result = "Volunteer cheated!"
    elif len(matches) > 1: result = "Bad magician!"
    else: result = matches.pop()
    print("Case #%d: %s" % (i+1, result))
