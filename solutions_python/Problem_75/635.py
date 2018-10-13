#! /usr/bin/python

import sys, os

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

def sortComb(c1,c2):
    if c1 < c2:
        return c1 + c2
    else:
        return c2 + c1

pos = 1
for c in range(cases):
    print(lines[pos].strip())
    info = lines[pos].strip().split()
    C = int(info[0])
    if C <> 0:
        C_str = ''.join(info[1:1+C])
        del info[0:1+C]
    else :
        del info[0]
    D = int(info[0])
    if D <> 0:
        D_str = ''.join(info[1:1+D])
        del info[0:1+D]
    else :
        del info[0]
    N, N_str = info
    combinations = {}
    for i in range(int(C)):
        combinations[ sortComb(C_str[i*3], C_str[i*3+1]) ] = C_str[i*3+2] 
    opposingElements = []
    for i in range(int(D)):
        opposingElements.append( sortComb(D_str[i*2], D_str[i*2+1]) )
    seq = N_str
    inputData.append([seq, combinations, opposingElements])
    print('seq, combinations, opposingElements')
    print(seq, combinations, opposingElements)
    pos = pos + 1


def analyse(seq, combinations, opposingElements):
    #print('seq, combinations, opposingElements')
    #print(seq, combinations, opposingElements)
    elements = []
    manifest = dict([[chr(65 + i),0] for i in range(26)])
    for s in seq:
        elements.append(s)
        manifest[s] =  manifest[s] + 1
        while len(elements) > 1 and \
                combinations.has_key(sortComb(elements[-1],elements[-2])) :
            e1, e2 = elements[-1], elements[-2]
            manifest[e1] =  manifest[e1] - 1
            manifest[e2] =  manifest[e2] - 1
            elements[-2] = combinations[ sortComb(e1,e2) ]
            manifest[elements[-2]] = manifest[elements[-2]] + 1
            del elements[-1]
        #check for opposing elements?
        shortList = [k for k,v in manifest.iteritems() if v > 0]
        if any([sortComb(m,elements[-1]) in opposingElements for m in shortList]):
            elements = []
            manifest = dict([[chr(65 + i),0] for i in range(26)])
        #print(elements, s, shortList)
    return str(elements).replace("'",'')

def analyse2(seq, combinations, opposingElements):
    elements = []
    for s in seq:
        elements.append(s)
        if len(elements) > 1 and combinations.has_key(sortComb(elements[-1],elements[-2])):
            elements[-2] = combinations[sortComb(elements[-1],elements[-2])]
            del elements[-1]
        #check for opposing elements?
        if any([sortComb(e,elements[-1]) in opposingElements for e in elements[:-1]]):
            elements = []
            manifest = []
    return str(elements).replace("'",'')

output = []
for case,input in enumerate(inputData[:]):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(*input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
