import string
import math

input = 'B-large.in'
output = 'output-b-large'
try:
    f = open(input, 'r')
except:
    exit('file: ' + input + ' non trovato')
try:
    out = open(output, 'w')
except:
    exit('file: ' + output + ' non trovato')

T = int(f.readline())

for index in range(T):
    l1 = f.readline()
    l2 = string.split(l1)
    
    C = int(l2[0])
    del l2[0]
    if C > 0:
        l3 = l2[:C]
        comb = {}
        for i in range(len(l3)):
            comb[l3[i][0] + l3[i][1]] = l3[i][2]
            i = i + 1
        del l2[:C]
        
    D = int(l2[0])
    del l2[0]
    if D > 0:
        l3 = l2[:D]
        opp = []
        for i in range(len(l3)):
            opp.append([l3[i][0], l3[i][1]])
            i = i + 1
        del l2[:D]

    N = int(l2[0])
    del l2[0]
    l3 = []
    i = 1
    l2 = l2[0]
    l3.append(l2[0])

    while i < len(l2):
        if C > 0 and len(l3) > 0 and l3[len(l3) - 1] + l2[i] in comb:
            new = comb[l3[len(l3) - 1] + l2[i]]
            l3.pop()
            l3.append(new)
        elif C > 0 and len(l3) > 0 and l2[i] + l3[len(l3) - 1] in comb:
            new = comb[l2[i] + l3[len(l3) - 1]]
            l3.pop()
            l3.append(new)
        else:
            l3.append(l2[i])
        i = i + 1
        if D > 0:
            for k in range(len(l3)):
                for m in range(len(l3)):
                    if k != m:
                        if [l3[k], l3[m]] in opp or [l3[m], l3[k]] in opp:
                            l3 = []
    
    out.write('Case #' + str(index + 1) + ': [')
    for x in range(len(l3)):
        if (x != 0):
            out.write(', ')
        out.write(str(l3[x]))
    out.write(']\n')
    