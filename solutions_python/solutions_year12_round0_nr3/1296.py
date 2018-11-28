#!/usr/bin/python
import sys
import os
import string

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
    
def calc(str1,str2):
    a=int(str1)
    b=int(str2)
    s=set()
    length = len(str1)
    for n in range(a,b):
        strn = str(n)
        for i in range(1,length):
            m = int(strn[-i:]+strn[:-i])
            if (n<m and m<=b):
               #print n, ' ', m
               s.add(strn+' '+str(m))
    return len(s)

if len(sys.argv) == 1:
    print('Bitte Eingabedatei als Aufrufparameter mitgeben')
else:
    lines_of_file = open_file(open(sys.argv[1], 'r'))
    new_data = translate_data(lines_of_file)
    write_file(open('output.dat', 'w'),new_data)
