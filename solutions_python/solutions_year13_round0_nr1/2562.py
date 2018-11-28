# -*- coding: utf-8 -*-

def listen(mas):        
    draw = True
    for slice in mas :
        if '.' in slice :
            draw = False 
        else :
            d = 1
            for j in range(1,4):
                if slice[0] == slice[j] or slice[j] == 'T':
                    d += 1
                if d == 4 :
                    return slice[0]
    if draw:
        return 'D'
    return 'G'

f1 = open('tt.in')
f2 = open('tt.out', mode = "w")
i = 0
ss = [False]*16
answer =[]
for line in f1 :
    i += 1
    line = line[:-1]
    if i==1 :
        T = int(line)
        k = 0
    else :
        if k != 4 :
            k+=1
        else:
            k = 0
            ss = [False]*16    
        st = line
        n = 0
        if k != 0:
            for c in st :               
                ss[(k-1)*4+n] = c
                n += 1
        if k == 4 :
            mas = []         
            mas.append([ss[0],ss[1],ss[2],ss[3]])
            mas.append([ss[4],ss[5],ss[6],ss[7]])
            mas.append([ss[8],ss[9],ss[10],ss[11]])
            mas.append([ss[12],ss[13],ss[14],ss[15]])
            mas.append([ss[0],ss[4],ss[8],ss[12]])
            mas.append([ss[1],ss[5],ss[9],ss[13]])
            mas.append([ss[2],ss[6],ss[10],ss[14]])
            mas.append([ss[3],ss[7],ss[11],ss[15]])
            mas.append([ss[0],ss[5],ss[10],ss[15]])
            mas.append([ss[3],ss[6],ss[9],ss[12]])
            answer.append(listen(mas))



                    

for i in range(T):
    if answer[i] == 'X' :
        st3 = 'X won' 
    if answer[i] == 'O' :
        st3 = 'O won' 
    if answer[i] == 'D' :
        st3 = 'Draw' 
    if answer[i] == 'G' :
        st3 = 'Game has not completed' 
    st2 = 'Case #' + str(i+1) + ': ' + st3 + "\n"    
    f2.write(st2)

f2.close()
f1.close()            