from math import ceil
f = open('A-small-attempt1.in', 'r')
fo = open('output.txt', 'w')
T = int(f.readline())
for caseID in range(T):
    line = f.readline().strip().split()
    N = int(line[0])
    P = int(line[1])
    Gs = f.readline().strip().split()
    G = [int(e) for e in Gs]
    mymap = {}
    total_number = 0
    for g in G:
        if g % P == 0:
            total_number += 1
            continue
        else:
            mod = g % P
            if mod not in mymap:
                mymap[mod] = 0
            mymap[mod] += 1
    if P == 2:
        if 1 in mymap:
            total_number += ceil(mymap[1]/2.0) 
    if P == 3:
        if 1 in mymap and 2 in mymap:
            num = min(mymap[1], mymap[2])
            total_number += num
            mymap[1] -= num
            mymap[2] -= num
            if mymap[1] == 0:
                del mymap[1]
            if mymap[2] == 0:
                del mymap[2]
        if 1 in mymap:
            total_number += ceil(mymap[1] / 3.0)
        if 2 in mymap:
            total_number += ceil(mymap[2] / 3.0)
    if P == 4:
        if 1 in mymap and 3 in mymap:
            num = min(mymap[1], mymap[3])
            total_number += num
            mymap[1] -= num
            mymap[3] -= num
            if mymap[1] == 0:
                del mymap[1]
            if mymap[3] == 0:
                del mymap[3]
        if 1 in mymap:
            total_number += ceil(mymap[1]/4.0)
        if 3 in mymap:
            total_number += ceil(mymap[3]/4.0)
        if 2 in mymap:
            total_number += ceil(mymap[2]/2.0)
    fo.write("Case #{}: {}\n".format(caseID+1, total_number))
f.close()
fo.close()