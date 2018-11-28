## Magician

import cj
import numpy as np

cases = cj.parse_cases(cj.ifile(), 1)
numcases = cj.get_num_cases(cj.ifile())

f = open('prob_a_sln.txt','w')

print cases
print numcases

numcases=int(numcases)

for n in range(numcases):
    row1=int(cases[n*10][0])
    row2=int(cases[n*10+5][0])
    cards1=np.zeros([4,4])
    cards2=np.zeros([4,4])

    cards1[0,:] = cases[(n*10+1)][0].split(" ")
    cards1[1,:] = cases[(n*10+2)][0].split(" ")
    cards1[2,:] = cases[(n*10+3)][0].split(" ")
    cards1[3,:] = cases[(n*10+4)][0].split(" ")

    cards2[0,:] = cases[(n*10+6)][0].split(" ")
    cards2[1,:] = cases[(n*10+7)][0].split(" ")
    cards2[2,:] = cases[(n*10+8)][0].split(" ")
    cards2[3,:] = cases[(n*10+9)][0].split(" ")

    cands1=cards1[row1-1,:]
    cands2=cards2[row2-1,:]

    inter = np.intersect1d(cands1, cands2);print inter



    if(len(inter)==1):
        to_print= r"Case #" + str(n+1) + ": " + str(int(inter[0])) + "\n"
    elif(len(inter)>1):
        to_print= r"Case #" + str(n+1) + ": Bad magician!\n" 
    else:
        to_print=r"Case #" + str(n+1) + ": Volunteer cheated!\n"
    f.write(to_print) 

f.close() 
