import sys
si = sys.stdin

T = int(si.readline())


for tcase in range(T):
    line = si.readline()
    tokens = line.split()

    C = int(tokens[0])
    combines = tokens[1:1+C]
    tokens = tokens[1+C:]
    D = int(tokens[0])
    opposed = tokens[1:1+D]
    tokens = tokens[1+D:]
    N = int(tokens[0])
    order = tokens[1]

    stack = []
    for i, el in enumerate(order):
        stack.append(el)
        if len(stack) >= 2:
            for comb in combines:
                if (comb[0], comb[1]) == (stack[-1], stack[-2]) \
                or (comb[0], comb[1]) == (stack[-2], stack[-1]):
                    stack = stack[:-2] + [comb[2]]
                    break
        for i in range(len(stack)-1):
            cel = stack[i]
            for op in opposed:
                if (stack[-1], cel) == (op[0], op[1]) \
                or (stack[-1], cel) == (op[1], op[0]):
                    stack = []
                    break
            if len(stack) == 0:
                break
    
    stack_str = ', '.join(stack)
    print "Case #%d: [%s]" % (tcase+1, stack_str)
