#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

p = infile.readline()

T = long(p)

t = 0

while t < T:
    t += 1
    C, D, N = 0, 0, 0
    element = []
    combine = {}
    opposed = {}

    params = infile.readline()

    L = params.split()

    C = long(L.pop(0))
    while (C > 0):
        combo = L.pop(0)
        combine[combo[0]+combo[1]] = combo[2]
        combine[combo[1]+combo[0]] = combo[2]
        C -= 1

    C = long(L.pop(0))
    while (C > 0):
        combo = L.pop(0)
        opposed[combo[0]] = combo[1]
        opposed[combo[1]] = combo[0]
        C -= 1

    C = long(L.pop(0))
    if (C > 0):
        invoke = L.pop(0)
        for x in invoke:
            found = 0
            if len(element) <= 0:
                element.append(x)
                continue
            Z = element[-1] + x
            if Z in combine.keys():
                element.pop(-1)
                element.append(combine[Z])
                found = 1
            else:
                if x in opposed.keys():
                    n = len(element)
                    while(n >= 0):
                        n -= 1
                        if (element[n] == opposed[x]):
                            #element = element[:n]
                            element = []
                            found = 1
                            break
            if not found:
                element.append(x)
            #print element
    str = "["
    last = ''
    if len(element) > 0:
        last = element.pop(-1)
    for s in element:
        str += s
        str += ", "
    str += last + "]"
    print 'Case #%d: %s' % (t, str)
    #print combine
    #print opposed
