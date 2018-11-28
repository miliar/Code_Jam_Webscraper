#! /usr/bin/python -tt
# -*- coding: utf-8 -*-



f = open('workfile','r')
fout = open('file_out','w')

num_test = int((f.readline()).strip())

for m in range(0,num_test):
    
    score_war = 0
    score_dwar = 0
    num_caillou = int(f.readline().strip())
    caillou_N = f.readline().split()
    caillou_K = f.readline().split()
    caillou_N = [float(i) for i in caillou_N]
    caillou_K = [float(i) for i in caillou_K]
    caillou_K.sort()
    caillou_N.sort()

    caillou_Ktemp = list(caillou_K)
    caillou_Ntemp = list(caillou_N)

    for n in range(0,num_caillou):
        values = [(n,a) for n,a in enumerate(caillou_Ktemp) if a > caillou_Ntemp[0]]

        caillou_Ntemp.pop(0)
        if(len(values) == 0):
            score_war += 1
            caillou_Ktemp.pop(0)
        else:
            caillou_Ktemp.pop(values[0][0])


            
    for n in range(0,num_caillou):
       if caillou_N[-1] > caillou_K[-1]:
           caillou_K.pop()
           caillou_N.pop()
           score_dwar += 1
       else:
           caillou_K.pop()
           caillou_N.pop(0)

    print str(score_war) +" "+ str(score_dwar)
    fout.write("Case #"+ str(m+1) +": "+ str(score_dwar)+" "+str(score_war)+"\n")


    

    
    
