#!/usr/bin/env python
#-*- coding:utf-8 -*-

filename = 'C-large.in'
file=open(filename)

'''
2
5
1 2 3 4 5
3
3 5 6
'''

'''
Case #1: NO
Case #2: 11
'''

def add_wrong(a,b):
    a=bin(a)[2:].zfill(30)
    b=bin(b)[2:].zfill(30)
    c=[]

    for i in range(len(a)):
        ones = 0
        if a[i]=='1': ones+=1
        if b[i]=='1': ones+=1
        
        digit = '1' if ones==1 else '0'
        c.append(digit)
       
    # teraz trzeba zamienić na liczbę
    return int(''.join(c), 2)
        
def sum_wrong(l):
    suma=0
    for el in l:
        suma = add_wrong(suma, el)
        
    return suma
        
#print add_wrong(12,5)
#print add_wrong(5,6)
#print add_wrong(3,6)

# skąd mam wiedzieć czy da się podzielić cukierki na 2 kupki wg wrong_add? parzystość też działa?
# chyba chodzi o to że on dodaje je po kolei : czyli in: 3 5 6, 3=5+6, 3+5=6 
# może jak posortuje elementy?

for case in range(int(file.readline())):

    file.readline() #rubbish
    elements = [int(element) for element in file.readline().split()]
    elements.sort()

    current_max = -1    
    for i in range(1,len(elements)):

        if sum_wrong(elements[:i]) == sum_wrong(elements[i:]):
            left = sum(elements[:i])
            right = sum(elements[i:])
            result = max(left,right)
            if result > current_max: current_max=result

    wynik = 'NO' if current_max<0 else current_max    
    
    print 'Case #%i: %s' % ( case+1, wynik)
    


