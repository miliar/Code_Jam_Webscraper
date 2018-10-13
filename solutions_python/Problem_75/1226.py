import logging
num_cases = int(raw_input())

for cnum in range(1, num_cases + 1):
    case = raw_input().split()
    c = int(case.pop(0))
    pairs = {}
    for _ in range(c):
        pair = case.pop(0)
        k = ''.join(sorted(pair[0:2]))
        pairs[k] = pair[2]
    d = int(case.pop(0))
    opposed = {}
    for _ in range(d):
        parts = sorted(case.pop(0))
        opposed[parts[0]] = parts[1]
        opposed[parts[1]] = parts[0]

    invoke = case[1]
#    print "DEBUG: invoke: %s" % invoke
    stack = []
    
    for element in invoke:
        stack.append(element)
        if len(stack) > 1:
            top = ''.join(sorted([stack[-1], stack[-2]]))
            if top in pairs:
                while top in pairs:
                    stack.pop()
                    stack.pop()
                    stack.append(pairs[top])
                    if len(stack) > 1:
                        top = ''.join(sorted([stack[-1], stack[-2]]))
                    else:
                        break
            elif (element in opposed and opposed[element] in stack):
                stack = []

    print "Case #%s: [%s]" % (cnum, ', '.join(stack))
