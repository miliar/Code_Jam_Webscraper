import sys

def solve_test(test):
    num_combines = int(test.pop(0))
    combinations = {}
    for i in range(num_combines):
        comb = test.pop(0)
        combinations[comb[0],comb[1]] = comb[2]
        combinations[comb[1],comb[0]] = comb[2]
    num_opposed = int(test.pop(0))
    opposed = set()
    for i in range(num_opposed):
        op = test.pop(0)
        opposed.add((op[0],op[1]))
        opposed.add((op[1],op[0]))
    test.pop(0)
    seq = (test.pop(0))
    elmlist = []
    for a in seq:
        if not elmlist:
            elmlist.append(a)
            continue
        b = elmlist[-1]
        if (a,b) in combinations:
            elmlist.pop()
            elmlist.append(combinations[(a,b)])
        elif any((a,x) in opposed for x in elmlist):
            elmlist = []
        else:
            elmlist.append(a)
    out = ', '.join(elmlist)
    out = '['+out+']'

    return out
    

sequence = sys.stdin.readlines()

numtests = int(sequence[0])
for i in range(numtests):
    print "Case #%d: %s" % (i+1,solve_test(sequence[i+1].split()))


