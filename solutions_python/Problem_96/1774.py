#!C:/Python32/python.exe
#
"""Google Code Jam 2012

Qualification Round
Problem B. Dancing With the Googlers
"""

import sys

__author__ = "daLord"

# FILENAME_INPUT = "B-test.in"
# FILENAME_INPUT = "B-small-attempt0.in"
FILENAME_INPUT = "B-large.in"
FILENAME_OUTPUT = "B-large.out"

def solve(line):
    parts = line.split()
    N = int(parts[0])
    S = int(parts[1])
    p = int(parts[2])
    if p == 0:
        return N
    a = (p - 1) * 3
    b = a - 1
    x = 0
    y = 0
    for g in [int(i) for i in parts[3:]]:
        if a < g:
            x += 1
        elif g == a or g == b:
            y += 1
    if p == 1:
        return x
    return x + min(S, y)
        
def main():
    out = "Case #%s: %s\n"
    with open(FILENAME_INPUT, "r") as rfp:
        with open(FILENAME_OUTPUT, "w") as wfp:
            i = 0 # Lines
            n = 1 # Cases
            sets = 0
            for line in rfp:
                if i == 0:
                    sets = int(line.strip())
                if 0 < i and i <= sets:
                    result = out % (n, solve(line))
                    print(result[:-1])
                    wfp.write(result)
                    n += 1
                i += 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
