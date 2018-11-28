#!C:/Python32/python.exe
#
"""Google Code Jam 2011

Qualification Round
Problem B. Magicka
"""

import sys

__author__ = "daLord"

# FILENAME_INPUT = "B-test.in"
# FILENAME_INPUT = "B-small-attempt0.in"
FILENAME_INPUT = "B-large.in"
FILENAME_OUTPUT = "B-large.out"

def makeOppose(input):
    ret = {}
    for group in input:
        for i in range(2):
            if group[i] not in ret:
                ret[group[i]] = []
            if group[(i + 1)%2] not in ret[group[i]]:
                ret[group[i]].append(group[(i + 1)%2])
    return ret

def solve(line):
    temp = line.split() # Stations

    c = int(temp[0])
    temp = temp[1:]
    combine = [[a[0]+a[1], a[2]] for a in [[e for e in b] for b in temp[:c]]]
    temp = temp[c:]

    d = int(temp[0])
    temp = temp[1:]
    tempOppose = [[e for e in a] for a in temp[:d]]
    oppose = makeOppose(tempOppose)
    temp = temp[d:]

    n = int(temp[0])
    temp = temp[1:]
    invoke = [char for char in temp[0]]

    ret = []
    for element in invoke:
        ret.append(element)
        noMatchInLastRound = False
        while 1 < len(ret) and not noMatchInLastRound:
            match = None
            for comb in combine:
                if ret[-1] == comb[0][0] and ret[-2] == comb[0][1] or ret[-1] == comb[0][1] and ret[-2] == comb[0][0]:
                    match = comb[1]
                    break
            if match is not None:
                ret[-2:] = [match]
            else:
                noMatchInLastRound = True
        if 1 < len(ret):
            if ret[-1] in oppose:
                clear = False
                for char in ret[:-1]:
                    if char in oppose[ret[-1]]:
                        clear = True
                        break
                if clear:
                    ret = []
    return "[%s]" % ", ".join(ret)
        
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
