#!C:/Python32/python.exe
#
"""Google Code Jam 2012

Qualification Round
Problem C. Recycled Numbers
"""

import sys

__author__ = "daLord"

# FILENAME_INPUT = "C-test.in"
FILENAME_INPUT = "C-small-attempt0.in"
# FILENAME_INPUT = "C-large.in"
FILENAME_OUTPUT = "C-small-attempt0.out"

def solve(line):
    parts = line.split()
    A = int(parts[0])
    B = int(parts[1])
    matches = {}
    ret = 0
    for i in range(A, B + 1):
        s = str(i)
        r = [0] + [int(s[:len(s) - k - 1]) for k in range(len(s) - 1)]
        for j in range(1, len(s)):
            if 0 < int(s[j]):
                i1 = int(s[j:] + s[:j])
                if i < i1 and i1 <= B:
                # print(s, s[j:] + s[:j])
                    #ret += 1
                    if i not in matches:
                        matches[i] = []
                    if i1 not in matches[i]:
                        matches[i].append(i1)
                        ret += 1
    return ret
        
def main():
    print("C")
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
