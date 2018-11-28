from collections import defaultdict

ifile = open('../input/B-large.in', 'r')
ofile = open('../output/B-large.out', 'w')

cases = int(ifile.readline())

for case in xrange(cases):
    combine = {}
    opposed = defaultdict(list)
    tokens = ifile.readline().split()
    tokens.reverse()     
    for i in xrange(int(tokens.pop())):
        triplet = tokens.pop()            
        combine[triplet[0:2]] = triplet[2]
        combine[triplet[1::-1]] = triplet[2]
    for i in xrange(int(tokens.pop())):
        couple = tokens.pop()  
        opposed[couple[0]].append(couple[1]) 
        opposed[couple[1]].append(couple[0])    
    tokens.pop() #skip
    spell = []
    elements = defaultdict(int)
    #ugly spaghetti code 
    for el in tokens.pop():
        if spell:
            prev = spell[-1]
            replacement = combine.get("%s%s" % (prev, el))
            if replacement:                
                elements[prev] = elements[prev] - 1;  
                spell[-1] = replacement
                elements[replacement] = elements[replacement] + 1
                continue          
            doclear = False                  
            for opel in opposed[el]:
                if elements[opel]:
                    doclear = True
                    break
            if doclear:
                spell = []
                elements.clear()
                continue                    
        spell.append(el)
        elements[el] = elements[el] + 1
    ofile.write('Case #%d: %s\n' % (case+1, str(spell).replace("'", '')))    