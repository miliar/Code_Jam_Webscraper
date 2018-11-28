#!/usr/bin/env python

import sys

def run_case(line, content):
    result = None

    guess1 = int(content[line])
    possible = set(content[line + guess1].split())
    guess2 = int(content[line + 5])
    possible = set(content[line + 5 + guess2].split()) & possible

    if len(possible) > 1:
        result = "Bad magician!"
    elif len(possible) == 0:
        result = "Volunteer cheated!"
    else:
        result = next(iter(possible))
    return result

if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    input = "input.txt"

try:
    with open(input) as f:
        content = f.readlines()
except:
    print("Can not find input file: %s" % input)
    sys.exit()

T = int(content[0])

case = line = 1
while case <= T:
    result = run_case(line, content)

    print("Case #%d: %s" % (case, result))
    line += 10
    case += 1
