'''
Created on 13-Apr-2013

@author: jp
'''

from math import sqrt,ceil,floor

if __name__ == '__main__':
    fin=open('./C-small-attempt2.in','r')
    fout=open('./output','w')
    
    cases=fin.readline()
    
    for i in range(1,int(cases)+1):
        case=fin.readline()
        limits=case.split(' ')
        count=0
        for j in range(int(ceil(sqrt(int(limits[0])))),int(floor(sqrt(int(limits[1]))))+1):
            temp=str(j)
            if temp[::-1]==temp:
                temp=str(j*j)
                if temp[::-1]==temp:
                    count+=1
        fout.write('Case #'+str(i)+': '+str(count)+'\n')