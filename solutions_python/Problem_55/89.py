#!/usr/bin/python3

fin = open("input.txt",'r')
fout = open("output.txt",'w')

T = int(fin.readline())
for i in range(T):
    R,k,N = map(int,fin.readline().split())
    g = list(map(int,fin.readline().split()))
    Ns = {}
    NS = []
    index = 0
    count = 0
    steps = 0
    while index not in Ns:
        Ns[index] = (steps,count)
        NS.append(count)
        c = 0
        ind = index
        while c+g[ind]<=k:
            c+=g[ind]
            ind = (ind+1)%N
            if ind==index:
                break
        index = ind
        steps += 1
        count += c

    prefix = NS[:Ns[index][0]]
    cycle = NS[Ns[index][0]:]
    prefix_count = cycle[0]
    cycle_count = count-prefix_count
    if R<len(prefix):
        res = prefix[R]
    else:
        res  = prefix_count
        R -= len(prefix)
        res += cycle_count*(R//len(cycle))
        R = R%(len(cycle))
        res += cycle[R]-prefix_count
    print ("Case #%d: %d"%(i+1,res),file=fout)
            
