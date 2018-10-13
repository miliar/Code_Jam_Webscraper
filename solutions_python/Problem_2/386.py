#!/usr/bin/python
from sys import *

Ncasos = int(stdin.readline())




for caso in range(Ncasos):
    
    hor_table=[]

    turn_time = int(stdin.readline())
    [Na, Nb] = stdin.readline().split()
    Na = int(Na)
    Nb = int(Nb)
    
    Ta = 0 #Number of trains LACKING at station A
    Tb = 0 #Number of trains LACKING at station B

    Ta_max = 0 # Maximum number of trains station A had to have
    Tb_max = 0 # Maximum number of trains station B had to have


    for hor in range(Na):
        rd = stdin.readline().split()
        h1 = int(rd[0][0:2])*60 + int(rd[0][3:5])
        h2 = int(rd[1][0:2])*60 + int(rd[1][3:5])
####
        #print `h1`+ " - " +`h2`
        hor_table.append( (h1, 1) ) #event type 1: train leaves station A
        #hor_table.append( (h2, 4) ) #event type 4: train arrives at station B
        hor_table.append( (h2+turn_time, 4) ) #event type 4: train ready at station B

    # Read B events
    for hor in range(Nb):
        rd = stdin.readline().split()
        h1 = int(rd[0][0:2])*60 + int(rd[0][3:5])
        h2 = int(rd[1][0:2])*60 + int(rd[1][3:5])
####
        #print `h1`+ " - " +`h2`
        hor_table.append( (h1, 3) ) #event type 3: train leaves station B
        #hor_table.append( (h2, 2) ) #event type 2: train arrives at station A
        hor_table.append( (h2+turn_time, 2) ) #event type 2: train arrives at station A

    hor_table.sort()

    last_minute = -1;
    for t in hor_table:
        minute = t[0]
        event = t[1]
####
        #print `minute/60`+":"+`minute-60*(minute/60)`,"->", event,

        ##Atualization due to minute change
        if minute>last_minute:
            if Ta_max<Ta: Ta_max = Ta
            if Tb_max<Tb: Tb_max = Tb
            last_minute = minute

        if event == 1:  # a train left A
            Ta = Ta+1
        if event == 2:  # a train arrived at A
            Ta = Ta-1

        if event == 3:  # a train left B
            Tb = Tb+1
        if event == 4:  # a train arrived at B
            Tb = Tb-1
####
        #print "  ",Ta, Tb

    print "Case #"+`caso+1`+":", Ta_max, Tb_max
        


