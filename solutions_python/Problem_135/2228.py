# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 07:44:35 2014

@author: Johnny
"""
def main():
    output = open('A-small-attempt0.out','w')
    with open('A-small-attempt0.in') as f:
        t = int(f.readline()[:-1])
        for i in range(t):
            r1 = int(f.readline()[:-1])
            m1 = []
            for j in range(4):
                m1.append([int(x) for x in f.readline()[:-1].split(' ')])
            r2 = int(f.readline()[:-1])
            m2 = []
            for j in range(4):
                m2.append([int(x) for x in f.readline()[:-1].split(' ')])
            
            common = list(set(m1[r1-1]) & set(m2[r2-1]))
            if len(common) == 1:
                output.write("Case #%d: %d\n" %(i+1, common[0]))
            elif len(common) == 0:
                output.write("Case #%d: Volunteer cheated!\n"%(i+1))
            else:
                output.write("Case #%d: Bad magician!\n" %(i+1))
    output.close()
     
main()
