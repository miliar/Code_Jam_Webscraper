# -*- coding: utf-8 -*-
f1 = open('war.in')
f2 = open('war.out', mode = "w")
i = 0
Naomi_turn = True
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        N_pre = []
        K_pre = []
    else:
        l = line.split(" ")
        if '.' in l[0] :
            if Naomi_turn :
                N_pre.append(l)
            else :
                K_pre.append(l)
            Naomi_turn ^= True    


N = []
K = []
for each_case in N_pre :
    N.append([])
    for bricks in each_case :
        N[-1].append(float(bricks))
for each_case in K_pre :
    K.append([])
    for bricks in each_case :
        K[-1].append(float(bricks))

N_W = []
K_W = []
N_DW = []
K_DW = []
for all in N :
    N_W.append(sorted(all))
    N_DW.append(sorted(all))
for all in K :
    K_W.append(sorted(all))
    K_DW.append(sorted(all))
points_W = []
points_DW = []
for i in range(T) :
    points = 0
    while(len(N_W[i])) :
        cur_n = N_W[i][0]
        if K_W[i][-1] < cur_n :
            points += 1
            K_W[i].pop(0)
        else :
            q = False
            t = 0
            while not q :
                if K_W[i][t] > cur_n :
                    q = True
                    K_W[i].pop(t)
                t += 1
        N_W[i].remove(cur_n)
    points_W.append(points)            

for i in range(T) :
    points = 0
    while(len(N_DW[i])) :
        cur_n = N_DW[i][0]
        if cur_n > K_DW[i][0] :
            points += 1
            K_DW[i].pop(0)
        else :
            K_DW[i].pop()
        N_DW[i].remove(cur_n)
    points_DW.append(points)

for i in range(T):  
    st2 = 'Case #' + str(i+1) + ': ' + str(points_DW[i]) + " "+ str(points_W[i]) + "\n"    
    f2.write(st2)

f2.close()
f1.close()  