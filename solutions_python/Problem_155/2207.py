# Leroy J Gary III
# lgary@andrew.cmu.edu

import sys

cases = 1000
out = ""

def intListify(string):
    ans = []
    for c in list(string):
        ans.append(int(c))
    return ans

def caseCheck(line):
    line = intListify(line)
    if 0 not in line:
        return 0
    zeroMet = False
    ans = [0]
    for k, val in enumerate(line):
        if val == 0:
            zeroMet = True
        elif val != 0 and zeroMet:
            if k <= sum(line[:k]):
                pass
            else:
                ans += [k - sum(line[:k])]
            zeroMet = False
    return max(ans)

with open(sys.argv[1], 'r') as ifile:
    for i, line in enumerate(ifile):
        if i == 0:
            cases = line
        elif i > cases:
            break
        else:
            iline = line.split()
            ans = caseCheck(iline[1])
            out += "Case #%d: %d\n" % (i, ans)
    ifile.close
    sys.stdout.write(out)
