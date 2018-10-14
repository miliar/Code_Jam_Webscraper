#!/usr/bin/env python

import sys
count = int(sys.stdin.readline())

for i in range(count):
    data = sys.stdin.readline().split()
    combine = {}
    delete = {}
    
    j = 0
    c = int(data[j])
    j += 1
    if c != 0:
        for k in range(c):
            datum = data[j]
            combine[datum[0]+datum[1]] = datum[2]
            combine[datum[1]+datum[0]] = datum[2]
            j +=1
    
    d = int(data[j])
    j +=1
    if d != 0:
        for k in range(d):
            datum = data[j]
            if datum[0] in delete:
                delete[datum[0]].append(datum[1])
            else:
                delete[datum[0]] = [datum[1]]
            
            if datum[1] in delete:
                delete[datum[1]].append(datum[0])
            else:
                delete[datum[1]] = [datum[0]]
            
            j+=1
    
    n = int(data[j])
    j +=1
    elements = data[j]
    s =[]
    char_count = {}
    for j in range(65, 91):
        char_count[chr(j)] = 0
    for k in range(n):
        char_count[elements[k]] += 1
        s.append(elements[k])
        addnext = False
        joins = 1
        while True:
            if len(s) < 2:
                break
            last = ''.join(s[-2:])
            if last in combine:
                char_count[last[0]] -= 1
                char_count[last[1]] -= 1
                s = s[:-2]
                c = combine[last]
                char_count[c] += 1
                s.append(c)
                joins +=1
            else:
                break
        
        a = ''.join(s)
        clear = False
        for c in delete:
            if c in a:
                for o in delete[c]:
                    if o in a:
                        clear = True
                        break
            if clear == True:
                s = []
                    
    print "Case #%i: %s" % (i+1, str(s).replace('\'', ''))

