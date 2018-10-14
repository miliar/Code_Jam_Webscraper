'''
Created on 13. 4. 2012.

@author: Dracon
'''
import re


def main():
    input2 = open('B-large.in','r')
    output = open('B-large.out','w')
    line = input2.readline()
    for i in range(0,int(line)):
        linija = input2.readline()
        linija = re.split(' ',linija)
        broj = int(linija[0])
        surprise = int(linija[1])
        min = int(linija[2])
        ukupno = 0
        for j in range(0,broj):
            kolicnik = int(linija[j+3]) // 3
            ostatak = int(linija[j+3]) % 3
            if kolicnik >= min:
                ukupno += 1
            elif ostatak > 0 and min == kolicnik + 1:
                ukupno += 1
            elif min == kolicnik + 1 and surprise > 0 and kolicnik > 0:
                ukupno += 1
                surprise -= 1
            elif ostatak == 2 and surprise > 0 and min == kolicnik + 2:
                ukupno += 1
                surprise -= 1
        output.write("Case #"+str(i+1)+": "+str(ukupno)+'\n')
                
        
        
        
       
if __name__ == '__main__':
    main()