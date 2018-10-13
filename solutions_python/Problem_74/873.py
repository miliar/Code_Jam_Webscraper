#!C:/Python32/python.exe
#
"""Google Code Jam 2011

Qualification Round
Problem A. Bot Trust
"""

import sys

__author__ = "daLord"

# FILENAME_INPUT = "A-test.in"
# FILENAME_INPUT = "A-small-attempt0.in"
FILENAME_INPUT = "A-large.in"
FILENAME_OUTPUT = "A-large.out"

def solve(line):
    a = {'O': 1, 'B': 1}
    temp = line.split() # Stations
    limit = int(temp[0])
    s = temp[1:]
    st = {'O': {}, 'B': {}}
    maxima = {'O': -1, 'B': -1}
    for i in range(0, len(s), 2):
        st[s[i]][i/2] = int(s[i+1])
        maxima[s[i]] = i/2
    n = 0 # Processed waypoints
    j = 0 # Steps
    while n < limit:
        pushedAButton = False
        for color in st:
            # Find next waypoint
            if n <= maxima[color]:
                nextway = n
                while nextway not in st[color]:
                    nextway += 1
                    # print("Finding next ...")
                if a[color] < st[color][nextway]:
                    a[color] += 1
                elif a[color] > st[color][nextway]:
                    a[color] -= 1
                elif a[color] == st[color][nextway] and n == nextway:
                    # print("%s presses %s" % (color, a[color]))
                    pushedAButton = True
        if pushedAButton:
            n += 1
        j += 1
    return j
        
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
