'''
Created on 14/04/2013

@author: david
'''

import sys

fn = "b-small.in"
fn = sys.argv[1] 
f = open(fn, "r")
T = int(f.readline().strip())

fout = open("resB.txt", "w")
for t in range(T):
    kk = [int(e) for e in f.readline().strip().split()]
    N, M = kk[0], kk[1]
    m = []
    for r in range(N):
        m.append(f.readline().strip().split())
    mr = []
    for c in range(M):
        mr.append([m[r][c] for r in range(N)])
    #print(m)
    #print(mr)
    can = True
    for r in range(N):
        for c in range(M):
            if max(m[r])>m[r][c] and max(mr[c])>m[r][c]:
                can = False
                break
        if can==False:
            break
    res="Case #{0}: {1}".format(t+1, "YES" if can==True else "NO")
    fout.write(res+"\n")
    print(res)     
        
fout.close()