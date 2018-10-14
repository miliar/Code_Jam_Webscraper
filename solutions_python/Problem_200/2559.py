import numpy as np
import sys
COUNTCASE = 1
if (len(sys.argv)==1):
    print('Required argument : sample file\n')
    exit()
result = open('result','w')
sample = open(sys.argv[1],'r')

def minus(L, index):
    if (L[index] == '0'):
        L[index] = '9'
        if (index-1 >= 0):
            minus(L, index-1)
    else :
        L[index]=str(int(L[index]) - 1)

def rm_zero(L):
    cut = 0
    while (L[cut] == '0'):
        cut+=1
    return L[cut:]

            
def fulfill_nine(L,index):
    for k in range (len(L[index:])):
        L[index+k]='9'


nblines = sample.readline()
for k in range (int(nblines)):
    list_current = list(str(sample.readline()))[:-1]
    list_current = rm_zero(list_current)
    k=0
    while k < (len(list_current)-1):
        if ((int(list_current[k]) > int(list_current[k+1])) ):
            list_current[k] = str(int(list_current[k]) - 1)
            fulfill_nine(list_current, k+1)
            k=-1
        k+=1
    list_current=rm_zero(list_current)
    result.write('Case #' + str(COUNTCASE) + ': '+''.join(list_current)+'\n')
    COUNTCASE += 1

result.close()
sample.close()
