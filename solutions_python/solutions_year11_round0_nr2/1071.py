n_cases = input()

for case in xrange(1, n_cases + 1):
    els = []
    
    inp = raw_input().strip().split()

    comb = {}
    n_combs = int(inp.pop(0))

    for _ in xrange(n_combs):
        in1, in2, out = inp.pop(0)
        comb[(in1, in2)] = out
        comb[(in2, in1)] = out

    opp = {}
    n_opp = int(inp.pop(0))

    for _ in xrange(n_opp):
        el1, el2 = inp.pop(0)
        opp[el1] = el2
        opp[el2] = el1

    stack = []

    for el in inp[-1]:
        if stack and (el, stack[-1]) in comb:
            stack[-1] = comb[(el, stack[-1])]
        elif opp.get(el, None) in stack:
            stack = []
        else:
            stack += [el]
    
    print "Case #%d: [%s]" % (case, ", ".join(stack))
