#!/usr/bin/env python

import sys

def run_case(line, content):
    C, F, X = [float(i) for i in content[line].split()]

    time = 0.0
    farms = 0
    while True:
        cps = farms*F + 2

        time_complete = X/cps
        time_complete_farm = C/cps + X/(cps+F)

        if(time_complete < time_complete_farm):
            return time + time_complete
        else:
            farms += 1
            time += C/cps

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
    line = case
    result = run_case(line, content)

    print("Case #%d: %s" % (case, result))
    case += 1
