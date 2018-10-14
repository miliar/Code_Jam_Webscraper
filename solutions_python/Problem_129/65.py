from collections import OrderedDict
import math

#fin = open('test.in', 'r') 
fin = open('A-small-attempt3.in', 'r')
T = int(fin.readline().rstrip())
caseNo = 0
fout = open('A-large.out', 'w')
for i in range(T):
    x = fin.readline().rstrip().split()
    N, M = int(x[0]), int(x[1])
    o, e = [], []
    due = 0
    for i in range(M):
        x = fin.readline().rstrip().split()        
        t1, t2, t3 = int(x[0]), int(x[1]), int(x[2])
        d = t2 - t1
        due += t3 * (N * d - (d - 1) * d // 2)
        
        for i in range(len(o)):
            if o[i][0] == t1:
                o[i][1] += t3
                break
            if o[i][0] > t1:
                o.insert(i, [t1, t3, 0, 0])
                break
        else:
            o.append([t1, t3, 0, 0])
        for i in range(len(o)):
            if o[i][0] == t2:
                o[i][2] += t3
                break
            if o[i][0] > t2:
                o.insert(i, [t2, 0, t3, 0])
                break
        else:
            o.append([t2, 0, t3, 0])
        r = 0
        for i in o:
            t = min(i[1], i[2])
            i[1] -= t
            i[2] -= t
            r += i[1] - i[2]
            i[3] = r
            
    print(o) 
    act = 0
    i = 0
    while i < len(o):
        if o[i][1] == 0:
            i += 1
            continue
        j = i
        no = o[i][3]
        while o[j][3] > 0:
            no = min(no, o[j][3])            
            j += 1
        d = o[j][0] - o[i][0]
        act += no * (N * d - (d - 1) * d // 2)
        o[i][1] -= no
        for x in range(i, j):
            o[x][3] -= no
        o[j][2] -= no
        #print(o)
    #print(due, act)
    caseNo += 1
    fout.write('Case #' + str(caseNo) + ': ' + str(due - act) + '\n')

fin.close()
fout.close()

