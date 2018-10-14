import sys

cin = sys.stdin
cin.next() # skip line saying number of cases

case = 0
for line in cin:
    case += 1
    line = line.strip().split(" ")
    line.reverse()
    C = int(line.pop())
    combine = {}
    opposed = []
    for i in range(C):
        ccc = line.pop()
        key = (ccc[0], ccc[1])
        key = tuple(sorted(key))
        combine[key] = ccc[2]

    D = int(line.pop())

    for i in range(D):
        dd = line.pop()
        opposed.append(dd)

    line.pop() # discard length
    invoke = line.pop()

    # print "invoke: ", invoke
    # print "combine: ", str(combine)
    # print "opposed: ", str(opposed)

    state = []

    for ch in invoke:
        state.append(ch)
        #print "checking for ", str(tuple(sorted(state[-2:])))
        if len(state) >= 2 and tuple(sorted(state[-2:])) in combine:
            replace = combine[tuple(sorted(state[-2:]))]
            state[-2:] = replace
        else:
            uniq = set(state)
            for opp in opposed:
                if opp[0] in uniq and opp[1] in uniq:
                    state = []
                    # print str(state)
    print("Case #%d: [%s]" % (case, ", ".join(state)))


