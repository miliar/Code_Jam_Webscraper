from math import *

def func(ac,aj,lc,lj):
    if ac == 0 and aj == 0:
        return 1
    
    lc.sort()
    lj.sort()
##    print('lc', lc)
##    print('lj',lj)

    exch = 0
    
    lc2 = []
    lj2 = []

    lc1 = []
    lj1 = []

    c_time = 720
    j_time = 720
    

    if len(lc) == 0:
        prev_act = lj.pop(0)
        j_time -= prev_act[1]-prev_act[0]
        lj1.append((prev_act[0],True))
        #exch += 1
        prev = 'j'
        starter = 'j'
    elif len(lj) == 0:
        prev_act = lc.pop(0)
        c_time -= prev_act[1]-prev_act[0]
        lc1.append((prev_act[0],True))
        #exch += 1
        prev = 'c'
        starter = 'c'
    elif lc[0][0] < lj[0][0]:
        prev_act = lc.pop(0)
        c_time -= prev_act[1]-prev_act[0]
        lc1.append((prev_act[0],True))
        #exch += 1
        prev = 'c'
        starter = 'c'
    else:
        prev_act = lj.pop(0)
        j_time -= prev_act[1]-prev_act[0]
        lj1.append((prev_act[0],True))
        #exch += 1
        prev = 'j'
        starter = 'j'
        #print('Hi there')

    first_act = prev_act


    while len(lc) != 0 or len(lj) != 0:
##        print('--------------')
##        print('lc', lc)
##        print('lj',lj)
##        print('exch',exch)
        
        if len(lc) == 0:
            act = lj.pop(0)
            j_time -= act[1]-act[0]
            if prev == 'j':
                lj2.append(act[0]-prev_act[1])
                exch += 2
            else:
                exch += 1
            prev = 'j'
            prev_act = act
                
        elif len(lj) == 0:
            act = lc.pop(0)
            c_time -= act[1]-act[0]
            if prev == 'c':
                lc2.append(act[0]-prev_act[1])
                exch += 2
            else:
                exch += 1
            prev = 'c'
            prev_act = act
        elif lc[0][0] < lj[0][0]:
            act = lc.pop(0)
            c_time -= act[1]-act[0]
            if prev == 'c':
                lc2.append(act[0]-prev_act[1])
                exch += 2
            else:
                exch += 1
            prev = 'c'
            prev_act = act
        else:
            act = lj.pop(0)
            j_time -= act[1]-act[0]
            if prev == 'j':
                lj2.append(act[0]-prev_act[1])
                exch += 2
            else:
                exch += 1
            prev = 'j'
            prev_act = act
##    print('lc2', lc2)
##    print('lj2',lj2)
    act = (first_act[0]+1440,first_act[1]+1440)
    
    if starter == 'j':
        if prev == 'j':
            lj2.append(act[0]-prev_act[1])
            exch += 2
        else:
            exch += 1
            
    else:
        if prev == 'c':
            lc2.append(act[0]-prev_act[1])
            exch += 2
        else:
            exch += 1

##    if prev == 'c':
##        lc1.append((1440 - prev_act[1],False))
##        exch += 1
##        ender = 'j'
##    else:
##        lj1.append((1440 - prev_act[1],False))
##        exch += 1
##        ender = 'c'
##
##    print('lc', lc)
##    print('lj',lj)
##    print('***c_time', c_time)
##    print('***j_time',j_time)
##    print('exch',exch)
##    print('lc1', lc1)
##    print('lj1',lj1)
##    print('lc2', lc2)
##    print('lj2',lj2)
    lc2.sort()
    lc1.sort()
    lj2.sort()
    lj1.sort()

    while c_time !=0 and len(lc2) != 0:
        if lc2[0] > c_time:
            break
        exch -= 2
        c_time -= lc2[0]
        lc2.pop(0)
##    while c_time !=0 and len(lc1) != 0:
##        if lc1[0][0] > c_time:
##            break
##        exch -= 1
##        c_time -= lc1[0][0]
##        if lc1[0][1]:
##            starter = 'c'
##        else:
##            ender = 'c'
##        lc1.pop(0)
##        
    while len(lc2) > 0 and lc2[0] == 0:
        lc2.pop(0)
        exch -= 2
##    while len(lc1) > 0 and lc1[0][0] == 0:
##        if lc1[0][1]:
##            starter = 'c'
##        else:
##            ender = 'c'
##        lc1.pop(0)
##        exch -= 1
##########
    while j_time !=0 and len(lj2) != 0:
        if lj2[0] > j_time:
            break
        exch -= 2
        j_time -= lj2[0]
        lj2.pop(0)
##    while j_time !=0 and len(lj1) != 0:
##        if lj1[0][0] > j_time:
##            break
##        exch -= 1
##        j_time -= lj1[0][0]
##        if lj1[0][1]:
##            starter = 'j'
##        else:
##            ender = 'j'
##        lj1.pop(0)
        
    while len(lj2) > 0 and lj2[0] == 0:
        lj2.pop(0)
        exch -= 2
##    while len(lj1) > 0 and lj1[0][0] == 0:
##        if lj1[0][1]:
##            starter = 'j'
##        else:
##            ender = 'j'
##        lj1.pop(0)
##        exch -= 1
##    print('starter',starter)
##    print('ender',ender)

##    if starter != ender:
##        exch -= 1
##    else:
##        print('lj1',lj1)
##        print('lc1',lc1)
##        print('starter',starter)
##        print('ender',ender)
##        if starter == 'c':
##            if lj1[0][0] + lj1[1][0] < j_time:
##                exch -= 2
##        else:
##            if lc1[0][0] + lc1[1][0] < c_time:
##                exch -= 2
            
    
    return exch

        


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    ac,aj = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    lc = []
    for j in range(ac):
        c,d = [float(f) for f in input().split(" ")]
        lc.append((c,d))
    lj = []
    for j in range(aj):
        c,d = [float(f) for f in input().split(" ")]
        lj.append((c,d))
    
    print("Case #{}: {}".format(i, func(ac,aj,lc,lj)))


    
