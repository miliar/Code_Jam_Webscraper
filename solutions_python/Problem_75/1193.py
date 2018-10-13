import sys

testn = int(sys.stdin.readline())

for i in range(1, testn+1):
    case = sys.stdin.readline()
    case = case.split()
    
    C = int(case[0])
    combs = dict([("".join(sorted(x[0:2])),x[2]) for x in case[1:1+C]])

    case = case[C+1:]

    D = int(case[0])
    dests = dict([("".join(sorted(x[0:2])),1) for x in case[1:1+D]])

    case = case[D+1:]

    N = case[0]
    seq = case[1]

    l = []
    for s in seq:
        l.append(s)
        if len(l) >= 2:

            if "".join(sorted(l[-1]+l[-2])) in combs:
                ap = combs["".join(sorted(l[-1]+l[-2]))]
                l.pop()
                l[-1] = ap

            else:
                for e in l[0:-1]:
                    if "".join(sorted(e+l[-1])) in dests:
                        l = []
                        break
    print 'Case #'+str(i)+': [' + ", ".join(l) + ']'
