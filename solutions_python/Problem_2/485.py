
try:
    import psyco 
    psyco.full()
except ImportError:
    print 'psyco is not imported!!'
import sys
import os
import math
import string
from copy import copy
import time


def get_M(filename):
    input_data=[]
    if os.path.exists(filename):
        Fin = open(filename,"r")
    else:
        print "can't open input file"
        return 0
    newline=0
    inline=Fin.readline()
    N=int(inline)
    
    A2B_TT = []
    B2A_TT = []
    for case_number in range(N):
        inline=Fin.readline()
        TAT=int(inline)
            
        inline=Fin.readline()
        NA = int(inline.split()[0])
        NB = int(inline.split()[1])
            
        del A2B_TT
        A2B_TT = []
        del B2A_TT
        B2A_TT = []

        for any_NA in range(NA):
            inline = Fin.readline()
            DTs=inline.split()[0]
            ATs=inline.split()[1]
            DT = int(DTs.split(':')[0])*60+int(DTs.split(':')[1])
            AT = int(ATs.split(':')[0])*60+int(ATs.split(':')[1])
            A2B_TT += [[DT, AT]]
                
        for any_NB in range(NB):
            inline = Fin.readline()
            DTs=inline.split()[0]
            ATs=inline.split()[1]
            DT = int(DTs.split(':')[0])*60+int(DTs.split(':')[1])
            AT = int(ATs.split(':')[0])*60+int(ATs.split(':')[1])
            B2A_TT += [[DT, AT]]
                
        input_data+=[[case_number, NA, NB, A2B_TT, B2A_TT, TAT]]
        
        
    return input_data


def numeric_compare(x, y):
    if x[0]>y[0]:
        return 1
    elif x[0]==y[0]:
        if x[1]>y[1]:
            return -1
        elif x[1]==y[1]:
            return 0
        else:
            return 1
        
    else: # x<y
        return -1

#**********************************************************
def cal_numberm_must_start(input_data):
    results=[]
    listA=[]
    listB=[]
    for case_number in range(len(input_data)):
        del listA
        del listB
        listA=[]
        listB=[]
        for A2B_TT in range(len(input_data[case_number][3])):
            if input_data[case_number][3][A2B_TT][0]<1440:
                listA+=[[input_data[case_number][3][A2B_TT][0],-1]]
            if input_data[case_number][3][A2B_TT][1]+input_data[case_number][5]<1440:
                listB+=[[input_data[case_number][3][A2B_TT][1]+input_data[case_number][5], 1]]
            
        for B2A_TT in range(len(input_data[case_number][4])):
            if input_data[case_number][4][B2A_TT][0]<1440:
                listB+=[[input_data[case_number][4][B2A_TT][0],-1]]
            if input_data[case_number][4][B2A_TT][1]+input_data[case_number][5]<1440:
                listA+=[[input_data[case_number][4][B2A_TT][1]+input_data[case_number][5], 1]]
        listA.sort(numeric_compare)
        listB.sort(numeric_compare)
        
        must_start_at_A=0
        t=0
        for time_stamp in listA:
            t+=time_stamp[1]
            if t<0:
                t=0
                must_start_at_A+=1
        
        must_start_at_B=0
        t=0
        for time_stamp in listB:
            t+=time_stamp[1]
            if t<0:
                t=0
                must_start_at_B+=1
        
        results+=[[case_number+1,must_start_at_A,must_start_at_B]]
    return results


#**********************************************************
def print_results(results,filename):
    
    filename=filename[:len(filename)-3]
    filename+=".out"
    Fout = open(filename,"w")
    
    for any_result in results:
        line="Case #%d"%any_result[0], ": %d"%any_result[1], " %d"%any_result[2]
        Fout.write(''.join(line))
        Fout.write('\n')
    Fout.close()


#**********************************************************
input_data=get_M(sys.argv[1])
results=cal_numberm_must_start(input_data)
print_results(results,sys.argv[1])
