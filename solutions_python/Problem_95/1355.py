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
    outtab = "abcdefghijklmnopqrstuvwxyz"
    intab  = "ynficwlbkuomxsevzpdrjgthaq"
    trantab = string.maketrans(intab, outtab)

    for i in range(1,len(lines)):
        new_lines.append('Case #'+str(i)+': '+lines[i].translate(trantab))
    return new_lines

if len(sys.argv) == 1:
    print('Bitte Eingabedatei als Aufrufparameter mitgeben')
else:
    lines_of_file = open_file(open(sys.argv[1], 'r'))
    new_data = translate_data(lines_of_file)
    write_file(open('output.dat', 'w'),new_data)
