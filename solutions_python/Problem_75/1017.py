def invoke(element):
    global elements
    if len(elements) > 0:
        if elements[-1] + element in combinations:
            elements.append(combinations[elements.pop()+element])
        elif element + elements[-1] in combinations:
            elements.append(combinations[element+elements.pop()])
        else:
            if element in opposite.keys() and opposite[element] in elements:
                elements = []
            else:
                elements.append(element)
    else:
        elements.append(element)
        
f = open("B-small-attempt0.in")
of = open("B-small-attempt0.out", 'w')
T = int(f.readline())
for i in range(T):
    elements = []
    opposite = {}
    combinations = {}
    line = f.readline().split(' ')
    
    C = int(line.pop(0))

    for j in range(C):
        cmb = line.pop(0)
        combinations[cmb[0]+cmb[1]] = cmb[2]
        combinations[cmb[1]+cmb[0]] = cmb[2]

    D = int(line.pop(0))

    for j in range(D):
        opp = line.pop(0)
        opposite[opp[0]] = opp[1]
        opposite[opp[1]] = opp[0]

    N = int(line.pop(0))
    
    seq = line.pop(0)
    for j in range(N):
        invoke(seq[j])

    of.write("Case #{0}: [{1}]\n".format(i+1, ", ".join(elements)))

of.close()
f.close()
    

    
