## Magician

import cj
import numpy as np

cases = cj.parse_cases(cj.ifile(), 1)
numcases = cj.get_num_cases(cj.ifile())

f = open('prob_c_sln.txt','w')

print cases
print numcases

numcases=int(numcases)

for n in range(numcases):
    num_blocks=int(cases[n*3][0])
    
    nao=np.zeros(num_blocks)
    ken=np.zeros(num_blocks)

    nao[:] = cases[(n*3+1)][0].split(" ")
    ken[:] = cases[(n*3+2)][0].split(" ")
    
    nao_s1= np.sort(nao)
    ken_s1= np.sort(ken)
    nao_s2=nao_s1
    ken_s2=ken_s1
    
    nao_p1=0
    
    for i in range(num_blocks):
        if(ken_s1[-1]>nao_s1[-1]):   #-- Ken wins
            ken_s1=np.delete(ken_s1,-1)
            nao_s1=np.delete(nao_s1,0)
        else:                     #--Nao wins
            nao_p1=nao_p1+1
            nao_s1=np.delete(nao_s1,-1)
            ken_s1=np.delete(ken_s1,-1)
            
    nao_p2=0
    
    for i in range(num_blocks):
        if(nao_s2[-1]>ken_s2[-1]):   #-- Nao wins
            nao_p2=nao_p2+1
            nao_s2=np.delete(nao_s2,-1)
            ken_s2=np.delete(ken_s2,0)
        else:                     #--Ken wins
            nao_s2=np.delete(nao_s2,-1)
            ken_s2=np.delete(ken_s2,-1)

    to_print= r"Case #" + str(n+1) + ": " + str(nao_p1) + " " + str(nao_p2) + "\n"
    f.write(to_print) 

f.close() 
