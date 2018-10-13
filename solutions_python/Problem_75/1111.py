#!/usr/bin/python
import sys

def solve(case,dictionary,opposed,invoke):
    elements = []

    for c in invoke:
#        print elements
        elements.append(c)
        
        if len(elements)>1:
            # is there a combinaison?
            combi = elements[-1]+elements[-2]
            if combi in dictionary:
                elements.pop()
                elements.pop()
                elements.append(dictionary[combi])
#                print elements
                
            # are there two opposed on the list
            elif c in opposed:
                for n in elements[:-1]:
                    if opposed[c]==n:
                        elements = []
                        break
#        print elements
        
    s = "Case #{0}: {1}".format(case,elements)
    s = s.replace('\'','')
    print s

data = sys.argv[1]
f = open(data)
T = -1
case = 1

for l in f:
    l.strip()
    if T<0:
        T = int(l)
        sys.stderr.write("Test cases {0}\n".format(T))
    else:
        # base -> combinaison
        dictionary = {}
        opposed = {}
        
        dat = l.split()
        C = int(dat[0])
        dat = dat[1:]
        while C>0:
            s = dat[0]
            c1 = s[0]
            c2 = s[1]
            combi = s[2]
            dictionary[c1+c2] = combi
            dictionary[c2+c1] = combi
            C -= 1
            dat = dat[1:]

        D = int(dat[0])
        dat = dat[1:]
        while D>0:
            s = dat[0]
            c1 = s[0]
            c2 = s[1]
            opposed[c1]=c2
            opposed[c2]=c1
            D -= 1
            dat = dat[1:]

        N = int(dat[0])
        invoke = dat[1]
        solve(case,dictionary,opposed,invoke)
        case += 1
            
f.close()    
