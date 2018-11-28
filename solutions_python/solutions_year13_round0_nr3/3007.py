#!/usr/bin/python
import sys
import os
import string
from math import sqrt

def open_file(file):
    file_to_open = file
    lines = file.readlines()
    file.close()
    return lines
    
def write_file(file, data):
     file_to_write = file
     file_to_write.writelines(data)
     file_to_write.close()
     return
     
def translate_data(lines):
    new_lines = []
    for i in range(1,len(lines)):
        a,b=lines[i].split()
        new_lines.append('Case #'+str(i)+': '+str(calc(a,b))+'\n')
    return new_lines
    
def is_palindrome(n):
    strn = str(n)
    length = len(strn)
    for i in range(length/2):
        if (strn[i] != strn[-(i+1)]):
            return False
    return True
    
def calc(str1,str2):
    a=int(str1)
    b=int(str2)
    counter=0
    #print "\n"
    for i in range(int(sqrt(a)),int(sqrt(b))+1):
        if (is_palindrome(i)):
            square=i**2
            if ((square >= a) & (square <=b) & (is_palindrome(square))):
                counter+=1
                #print i, " ",i**2
    return counter
    

if len(sys.argv) == 1:
    print('Bitte Eingabedatei als Aufrufparameter mitgeben')
else:
    lines_of_file = open_file(open(sys.argv[1], 'r'))
    new_data = translate_data(lines_of_file)
    write_file(open('output.dat', 'w'),new_data)
