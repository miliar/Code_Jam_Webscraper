import os, sys

def solve(combine, oppose, invoke):
    l = []
    for i in invoke:
        if len(l) == 0: 
            l.append(i)
        else:
            last = l[len(l) - 1]
            c = last + i
            if c in combine:
                l[len(l) - 1] = combine[c]
            else:
                if i in oppose:
                    o_list = oppose[i]
                    cleared = False
                    for s in l:
                        if s in o_list:
                            l = []
                            cleared = True
                            break
                    if not cleared: l.append(i)
                else:
                    l.append(i)
    result = '['
    first = True
    for s in l:
        if not first: 
            result += ", " + s 
        else:
            result += s
            first = False
    result += ']'
    return result
    
                
            

nCases = int(sys.stdin.readline())

for case in range(1, nCases + 1):
    combine = {}
    oppose = {}
    invoke = []
    args = sys.stdin.readline().split()
    nCombines = int(args[0])
    start = 1
    next = start + nCombines
    for i in range(start, next):
        c = args[i]
        c1 = c[0] + c[1]
        c2 = c[1] + c[0]
        combine[c1] = c[2]
        combine[c2] = c[2]

    nOpposes = int(args[next])
    start = next + 1
    next += (nOpposes + 1)
    for i in range(start, next):
        c = args[i]
        if not c[0] in oppose: oppose[c[0]] = []
        if not c[1] in oppose: oppose[c[1]] = []
        oppose[c[0]].append(c[1])
        oppose[c[1]].append(c[0])
    
    invoke = args[next + 1]
    print "Case #" + str(case) + ": " + str(solve(combine, oppose, invoke))
    
