#!/usr/bin/python







out = open('output.dat','w')
f = open('o.test','r')


l = f.readline()
for i in range(0,int(l)):
    case = f.readline()
    case = case.split();

    evoke = list();

    c = int(case[0])
    r = int(case[1+c])
    e = int(case[2+r+c])
    combines = dict()
    removes = dict()
    for j in range(0,c):
        temp = case[j+1]
        for k in range(0,2):
            b = temp[k]
            s = temp[int(not(k))]
            if b in combines:
                combines[b][s] = temp[2]
            else:
                combines[b] = dict()
                combines[b][s] = temp[2]
    for j in range(0,r):
        temp = case[c+2+j]
        for k in range(0,2):
            b = temp[k]
            s = temp[int(not(k))]
            if b in removes:
                removes[b][s] = 1
            else:
                removes[b] = dict()
                removes[b][s] = 1
    temp = case[3+c+r]
    for j in range(0,e):
        element = temp[j]
        
        bail = 0
        if len(evoke) > 0:
            if element in combines:
                if evoke[len(evoke)-1] in combines[element]:
                    replace = combines[element][evoke[len(evoke)-1]]
                    evoke[len(evoke)-1]=replace
                    bail = 1
            if bail ==0:
                for k in range(0,len(evoke)):
                    if element in removes and bail ==0:
                        if evoke[k] in removes[element]:
                            evoke = list()
                            bail = 1
        if bail == 0:
            evoke.append(element)


    out.write('Case #' + str(i+1) + ': '+str(evoke).replace('\'','')+'\n')
