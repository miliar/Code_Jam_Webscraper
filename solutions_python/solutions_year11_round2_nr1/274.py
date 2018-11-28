#!C:/Python32/python.exe
#
"""Google Code Jam 2011

Round 1B
Problem A. Bot Trust
"""

import sys

__author__ = "daLord"

# FILENAME_INPUT = "A-test.in"
# FILENAME_INPUT = "A-small-attempt0.in"
FILENAME_INPUT = "A-large.in"
FILENAME_OUTPUT = "A-large.out"

def solve(inp):
    raw_ret = {}
    for i in range(len(inp)):
        raw_ret[i] = {}
        raw_ret[i]["games"] = dict([(c, int(inp[i][c])) for c in range(len(inp[i])) if inp[i][c] in ["0","1"]])
        raw_ret[i]["WP"] = sum(raw_ret[i]["games"].values())/len(raw_ret[i]["games"])
    for i in range(len(inp)):
        a = []
        for j in raw_ret[i]["games"]:
            temp = raw_ret[j]["games"]
            theirGames = [temp[c] for c in temp if c != i]
            a.append(sum(theirGames)/len(theirGames))
        #print(a)
        raw_ret[i]["OWP"] = sum(a)/len(a)
        #print(raw_ret[i]["OWP"])
    for i in range(len(inp)):
        a = []
        for j in raw_ret[i]["games"]:
            a.append(raw_ret[j]["OWP"])
        raw_ret[i]["OOWP"] = sum(a)/len(a)
    return "\n"+"\n".join([str(0.25 * raw_ret[i]["WP"] + 0.50 * raw_ret[i]["OWP"] + 0.25 * raw_ret[i]["OOWP"]) for i in range(len(raw_ret))])
        
def main():
    out = "Case #%s: %s\n"
    with open(FILENAME_INPUT, "r") as rfp:
        with open(FILENAME_OUTPUT, "w") as wfp:
            i = 0 # Lines
            j = -1 # Teams
            n = 1 # Cases
            inp = []
            sets = 0
            for line in rfp:
                if i == 0:
                    sets = int(line.strip())
                if 0 < i and n <= sets:
                    if j < 0:
                        j = int(line.strip())
                        inp = []
                    else:
                        inp.append(line.strip())
                i += 1
                j -= 1
                if j == -1:
                    result = out % (n, solve(inp))
                    print(result[:-1])
                    wfp.write(result)
                    n += 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
