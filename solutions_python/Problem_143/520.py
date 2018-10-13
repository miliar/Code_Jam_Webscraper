# -*- coding: utf-8 -*-
AND = []
for i in range(1000) :
    AND.append([])
    for j in range(1000) :
        AND[i].append(i&j)

f1 = open('lottery.in')
f2 = open('lottery.out', mode = "w")
i = 0
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        A = []
        B = []
        K = []
    else:
        l = line.split(" ")
        A.append(int(l[0]))
        B.append(int(l[1]))
        K.append(int(l[2]))

for i in range(T):
    res = 0
    for j in range(A[i]) :
        for k in range(B[i]) :
            if AND[j][k] < K[i] :
                res += 1
    st2 = 'Case #' + str(i+1) + ': ' + str(res) + "\n"    
    f2.write(st2)

f2.close()
f1.close()  