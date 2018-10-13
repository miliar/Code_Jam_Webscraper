# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:14:14 2015

@author: Ezequiel
"""
from sys import stdin

def main():
    T = int(stdin.readline())
    for i in range(T):
        aux = stdin.readline().replace('\n','').split(' ')
        Smax = int(aux[0])
        people = aux[1]
        guests = 0
        standing = 0
        shyness = 0
        for cant in people:
            cant = int(cant)
            #if i == 1:
            #    print cant,shyness,standing
            # 110011
            if cant>0:
                if shyness<=standing:
                    standing += cant
                else:
                    c = shyness-standing
                    guests += c
                    standing += cant+c
            if shyness<Smax:
                shyness += 1
        
        #print guests,standing
        print 'Case #'+str(i+1)+': '+str(guests)


if __name__=='__main__':
    main()