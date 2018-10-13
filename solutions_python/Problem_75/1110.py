'''
Created on 7 mai 2011

@author: nicolas
'''

import sys

def solve(n, c, o, invoke):

    combine = {}
    for s in c:
        combine[s[0:2]] = s[2]
        combine[s[0:2][::-1]] = s[2]
    
    opposed = {}
    for s in o:
        opposed[s[0]] = s[1]
        opposed[s[1]] = s[0]
    #print opposed
    
    elements = []
    
    for el in invoke:
        elements.append(el)

        if combine.has_key(''.join(elements[-2:])):
            # Elements combine
            result = combine[''.join(elements[-2:])]
            elements.pop()
            elements.pop()
            elements.append(result)
        elif opposed.has_key(el) and opposed[el] in elements:
            # Elements are opposed
            elements = []
            
    print 'Case #{}: {}'.format(n, str(elements).replace("'", ''))


if __name__ == '__main__':
    filepath = sys.argv[1]
    file = open(filepath)
    
    file.readline()

    for t,line in enumerate(file.readlines()):
        l = line.split(None)
        l.reverse()
        
        combine = []
        opposed = []
        
        c = int(l.pop())
        for i in range(c):
            combine.append(l.pop())
        
        d = int(l.pop())
        for i in range(d):
            opposed.append(l.pop())
        
        n = int(l.pop())
        invoke = l.pop()
        
        solve(t+1, combine, opposed, invoke)
