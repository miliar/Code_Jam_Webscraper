import re,sys

base = ['Q','W','E','R','A','S','D','F']

numCases = int(sys.stdin.readline())
cases = []

def toString(list):
    out = '['
    for thing in list:
        out = out + thing + ', '
    if len(list) != 0:
        out = out[:len(out) - 2]
    return out + ']'


for n in range(numCases):
    cases.append(re.split(r'\s+',sys.stdin.readline().strip()))

i = 1
for case in cases:
    combine = {}
    oppose = []
    final = []
    C = int(case[0])
    case = case[1:]
    for c in range(C):
        chars = case[0]
        baseChar1 = chars[0]
        baseChar2 = chars[1]
        newChar = chars[2]
        combine[baseChar1 + baseChar2] = newChar
        combine[baseChar2 + baseChar1] = newChar
        case = case[1:]
    D = int(case[0])
    case = case[1:]
    for d in range(D):
        chars = case[0]
        oppose.append((chars[0],chars[1]))
        case = case[1:]
    N = int(case[0])
    for n in range(N):
        final.append(case[1][n])
        if len(final) > 1:
            if combine.has_key(final[len(final) - 1] + final[len(final) - 2]):
                hold = combine[final[len(final) - 1] + final[len(final) - 2]]
                final = final[:len(final) - 2]
                final.append(hold)
            for tuple in oppose:
                if tuple[0] in final and tuple[1] in final:
                    final = []
    print "Case #" + str(i) + ": " + toString(final)
    i = i + 1
