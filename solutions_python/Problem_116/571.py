'''
Created on 13/04/2013

@author: david
'''

import sys

fn = "a-small.in"
fn = sys.argv[1] 
f = open(fn, "r")
T = int(f.readline().strip())

fout = open("resA.txt", "w")
for t in range(T):
    m = []
    for i in range(4):
        m.append(f.readline().strip())
    #print(m)
    isFull = True
    mr = set()
    for lin in m:
        if '.' in lin: isFull=False
        mr.add("".join(sorted(list(lin))))
    for c in range(4):
        mr.add("".join(sorted([m[r][c] for r in range(4)])))
    mr.add("".join(sorted([m[d][d] for d in range(4)])))  
    mr.add("".join(sorted([m[d][3-d] for d in range(4)])))  
    wonX = 'TXXX' in mr or 'XXXX' in mr
    wonO = 'OOOT' in mr or 'OOOO' in mr

    if wonX or wonO:
        cad = "X won" if wonX else "O won"
    elif isFull:
        cad = "Draw"
    else:
        cad = "Game has not completed"
    res = "Case #{0}: {1}".format(t+1, cad)
    fout.write(res+"\n")
    print(res)
    f.readline()
fout.close()