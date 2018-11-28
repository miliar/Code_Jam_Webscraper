'''
Created on 13. 4. 2012.

@author: Dracon
'''
import re
from collections import deque


def main():
    input2 = open('C-small-attempt0.in','r')
    output = open('C-small-attempt0.out','w')
    line = input2.readline()
    for i in range(0,int(line)):
        linija = input2.readline()
        brojevi = re.split(' ',linija)
        minimum = int(brojevi[0])
        maksimum = int(brojevi[1])
        ukupno = 0
        for j in range(minimum,maksimum+1):
            if j > 9 :
                broj = j
                broj_pom = str(broj)
                for k in range(0,len(str(broj))-1):
                    broj3 = deque(broj_pom)
                    broj3.rotate(1)
                    broj2 = list(broj3)
                    broj2 = ''.join(broj2)
                    if int(broj2) <= maksimum and int(broj2) > broj :
                        ukupno += 1
                    broj_pom = broj2[:]
        output.write('Case #'+str(i+1)+': '+str(ukupno)+'\n')
                
        
        
        
       
if __name__ == '__main__':
    main()