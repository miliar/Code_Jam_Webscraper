# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:10:20 2017

@author: Justin Guirautane
"""


import os,time

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Tidy Number')

file = open("B-large.in",'r')
text = file.read()
monfichier = open("output_large.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])

def digits_in_N (N):
    digitsInN = []
    for i in str(N):
        digitsInN.append(int(i))
    return digitsInN
    

def is_tidy(number):
    l = digits_in_N(number)
    
    s = sorted(l)
    if l == s:
        return True
    else:
        return False
        
        


    


def find_tidy (number):
    number
    while is_tidy(number) != True:        
        number -= 1        
    return number


#print(find_tidy(271302))

def find_tidy2(number):
    liste = digits_in_N(number)
    final = []
    while is_tidy(number) != True:
        for i in range (0,len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i] -= 1
                for j in range (i+1, len(liste)):
                    liste[j] = 9
                nb = map(str, liste)
                number = int(''.join(nb))
                #print(number)
                break
    return number
  

#begin = time.time()  
#print(find_tidy2(111111111111111110))
#print(time.time() - begin)

        
        
        
        
        
        
        

def main():
    
    for i in range (1, number_of_cases+1):
        ans = find_tidy2 (int(lines[i]))
        monfichier.write("Case #"+str(i)+':'+' '+str(ans)+"\n")

begin = time.time()
main()
print(time.time()-begin)

monfichier.close()
file.close()