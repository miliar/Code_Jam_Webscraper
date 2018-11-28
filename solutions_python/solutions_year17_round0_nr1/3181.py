# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:54:01 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Oversized Pancake Flipper')

file = open("A-small-attempt1.in",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')
number_of_cases = int(lines[0])

def get_info(caseNb):
    #ligne en string
    pancakes = lines[caseNb].split(' ')[0]
    flipper = int(lines[caseNb].split(' ')[1])
    longueur = len(pancakes)
    return pancakes, flipper, longueur
    
def unCoup (pancakes, flipper, longueur):
    
    result = []
    pancakes = list(pancakes)
    nbrCombinaisons = longueur - flipper + 1
    
    for combi in range (nbrCombinaisons):
        
        combinaison = pancakes[:]
        
        for flip in range (combi, combi+flipper):
            
            if pancakes[flip] == '+':
                combinaison[flip] = '-'
            else:
                combinaison[flip] = '+'
                
        
        result.append(''.join(combinaison))
        
    return result
    
     
def calcul(caseNb):
    pancakes, flipper, longueur = get_info(caseNb)
    C = 0
    result = []
    if pancakes == longueur*'+':
        return 0
        
    else:
        
        #first try
        combi = unCoup(pancakes,flipper,longueur)
        
        C += 1
        while longueur*'+' not in combi and C < 8:
            for i in combi:
                result += unCoup (i,flipper,longueur)
            combi = result[:]
            C += 1
            
        if C>8:
            return "IMPOSSIBLE"
        else:
            return C
        


def flip(pancakes,longueur,flipper,indice):
    result = list(pancakes)
    if indice > longueur - flipper:
        indice = longueur - flipper
    for i in range (indice, indice+flipper):
        if result[i] == '+':
            result[i] = '-'
        else:
            result[i] = '+'
    return ''.join(result)












def cirat(caseNb):
    pancakes, flipper, longueur = get_info(caseNb)
    C = 0
    listePan = list(pancakes)
    result = listePan[:]
    
    if pancakes == '+'*longueur:
        return 0
    
    
    
    
    while result != '+'*longueur and C <= 100:
        for i in range (longueur):
            if result[i] == '-':
                result = flip(result,longueur,flipper,i)
                C += 1
                #print(result)
                break
    
    if C > 10:
        return 'IMPOSSIBLE'
    else:
        return C
        
    
            











           
def main():
    for cases in range (1,number_of_cases+1):
        C = cirat(cases)
        print('Case #'+str(cases)+' : '+str(C))
        monfichier.write("Case #"+str(cases)+':'+' '+str(C)+"\n")              

  
main()              
file.close()
monfichier.close()

     

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
