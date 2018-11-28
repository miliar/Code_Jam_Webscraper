#!/usr/bin/python -tt

import sys
import random
import copy
  



def main():
    f = open('q:\\codejam\\A-small-attempt1.in')
    out = open('q:\\codejam\\A-small-attempt1.out','w')
    
    testcases = int(f.readline())
    print('testcases = ', testcases)

    for tc in range(1, testcases + 1):
        print ('test case #', tc)
        line = f.readline()
        line = line.split()
        maxShyness = int(line[0])
        people = [int(x) for x in line[1]]
        print('ms = ', maxShyness, ' people = ', people)
        
        totalPeople = 0
        needToAddPeople = 0
        for shyness in range(0, maxShyness + 1):
            print('shyness = ', shyness, ' totalPeople = ', totalPeople)
            if (shyness > totalPeople) and (people[shyness] > 0):
                needToAddPeople += shyness - totalPeople
                totalPeople += needToAddPeople + people[shyness]                
            else:
                totalPeople += people[shyness]
            print('totalPeople = ', totalPeople, ' needToAdd = ', needToAddPeople)

        print('Case #'+str(tc)+': '+str(needToAddPeople)+'\n')
        out.write('Case #'+str(tc)+': '+str(needToAddPeople)+'\n')
            
    f.close()
    out.close()   
    


if __name__ == '__main__':
  main()
