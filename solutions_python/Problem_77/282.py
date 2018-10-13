#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

filename = 'D-small-attempt1.in'
file=open(filename)

'''
3
2
2 1
3
1 3 2
4
2 1 4 3
'''

'''
Case #1: 2.000000
Case #2: 2.000000
Case #3: 4.000000
'''

reps = 10000
# które najlepiej przytrzymać? te które pasują, resztę podrzucić/shuffle
    
for case in range(int(file.readline())):

    file.readline() #rubbish
    elements = [int(element) for element in file.readline().split()]
    posortowana = sorted(elements)
    
#    print elements, posortowana
    
    summary_cost = 0

    for k in range(reps):    
        cost = 0
        tablica = elements[:]
        
        while tablica!=posortowana:
            
            bajzel=[]
            
            for i in range(len(tablica)):
                if tablica[i] != i+1:
                    bajzel.append(tablica[i])
                    tablica[i]='_'
                    
            #print tablica         
            random.shuffle(bajzel)
            
            #teraz trzeba wstawić elementy
            
            for i in range(len(tablica)):
                if tablica[i] == '_':
                    tablica[i] = bajzel.pop(0)
            
            cost +=1        
            
        summary_cost += cost
    
    average_cost = round(float(summary_cost)/reps)
    
    
    print 'Case #%i: %f' % ( case+1, average_cost)
    


