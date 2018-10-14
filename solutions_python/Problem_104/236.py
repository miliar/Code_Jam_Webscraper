'''
Created on 05.05.2012

@author: Frederik Knust
'''

import itertools

filename = 'C-small-attempt0'

f = open(str.format('C:\Users\Freddy\Workspaces\Python\CodeJam\Round1B\{0}.in', filename))
o = open(str.format('C:\Users\Freddy\Workspaces\Python\CodeJam\Round1B\{0}.out', filename), 'w')

t = int(f.readline())

for i in range(t):
    l = f.readline()
    l = l.replace('\n', '')
    
    values = l.split(' ');
    n = int(values[0])
    values.pop(0)
    
    v = []
    for value in values:
        v.append(int(value))
        
    found = False
    firstSet = {}
    secondSet = {}
        
    for j in range(n):
        for combination in itertools.combinations(v, j+1):
            subsum = sum(combination)
            combinationset = set(combination)
            for k in range(j, n):
                for secondCombination in itertools.combinations(v, k+1):
                    if subsum == sum(secondCombination):
                        if combinationset != set(secondCombination):
                            found = True
                            firstSet = combinationset
                            secondSet = set(secondCombination)
                            break
                
                if found:
                    break
            if found:
                break
        if found:
            break
        
    out = str.format("Case #{0}:", i+1)
    o.write(out)
    o.write("\n")
    
    print out
    
    if found:
        out = ""
        for d in firstSet:
            out += str(d)
            out += " "
            
        out = out.strip()
        o.write(out)
        o.write("\n")
        print out
        
        out = ""
        for d in secondSet:
            out += str(d)
            out += " "
            
        out = out.strip()
        o.write(out)
        o.write("\n")
        print out
    else:
        out = "Impossible"
        o.write(out)
        o.write("\n")
        print out
            