'''
Created on May 7, 2011

@author: ratchet
'''

import sys

f = "B-small-attempt0.in"
if len(sys.argv) == 2:
    f = sys.argv[1]
    
file = open(f,"r")

t=int(file.readline())


for ln in range(t):
    cl = None
    op = None
    comb = {}
    clear = {}
    l = file.readline().strip().split(" ")
    c = int(l[0])
    cl = l[1:1+c]
    for i in cl:
        comb["".join(sorted(list(i[:2])))]=i[2]
    d = int(l[1+c])
    op = l[2+c:2+c+d]
    
    for i in op:
        ops = list(i)
        if clear.has_key(ops[0]):
            clear[ops[0]].append(ops[1])
        else:
            clear[ops[0]]=[ops[1]]
            
        if clear.has_key(ops[1]):
            clear[ops[1]].append(ops[0])
        else:
            clear[ops[1]]=[ops[0]]
        
    N = int(l[2+c+d])
    inv = l[3+c+d:][0]
    
#    print c,comb
#    print d,op
#    print N,inv

#    print comb
#    print clear
#    print inv
    
    el = []
#    print inv
    for i in range(N):
        el.append(inv[i])
        if len(el) > 1:
            last = "".join(sorted(el[-2:]))
            if comb.has_key(last):
#                print "combine",last,comb[last]
                el.pop()
                el.pop()
                el.append(comb[last])
            else:
                last = el[-1]
                for item in el[:-1]:
                    if clear.has_key(last):
                        if item in clear[last]:
                            el = []

    print "Case #%d:"%(ln+1),str(el).replace("'","")
#    break
file.close()