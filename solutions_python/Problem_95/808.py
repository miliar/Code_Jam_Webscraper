'''
Google Code Jam 2012, Qualification Round
Problem A
Created on Apr 13, 2012

@author: Gabriel D. Holodak
'''
import math
fin = open('A-small-attempt0.in')
fout = open('output.txt', 'w')
num_cases = int(fin.readline().strip())

for i in range(num_cases):
    output_string = 'Case #'+str(i+1)+": "
    
    words = fin.readline().strip().lower().split()
    
    for single_word in words:
        for single_letter in single_word:
            if single_letter == 'a':
                single_letter = 'y'
            elif single_letter == 'b':
                single_letter = 'h'
            elif single_letter == 'c':
                single_letter = 'e'
            elif single_letter == 'd':
                single_letter = 's'
            elif single_letter == 'e':
                single_letter = 'o'
            elif single_letter == 'f':
                single_letter = 'c'
            elif single_letter == 'g':
                single_letter = 'v'
            elif single_letter == 'h':
                single_letter = 'x'
            elif single_letter == 'i':
                single_letter = 'd'
            elif single_letter == 'j':
                single_letter = 'u'
            elif single_letter == 'k':
                single_letter = 'i'
            elif single_letter == 'l':
                single_letter = 'g'
            elif single_letter == 'm':
                single_letter = 'l'
            elif single_letter == 'n':
                single_letter = 'b'
            elif single_letter == 'o':
                single_letter = 'k'
            elif single_letter == 'p':
                single_letter = 'r'
            elif single_letter == 'q':
                single_letter = 'z'
            elif single_letter == 'r':
                single_letter = 't'
            elif single_letter == 's':
                single_letter = 'n'
            elif single_letter == 't':
                single_letter = 'w'
            elif single_letter == 'u':
                single_letter = 'j'
            elif single_letter == 'v':
                single_letter = 'p'
            elif single_letter == 'w':
                single_letter = 'f'
            elif single_letter == 'x':
                single_letter = 'm'
            elif single_letter == 'y':
                single_letter = 'a'
            elif single_letter == 'z':
                single_letter = 'q'
            output_string += single_letter
        output_string += ' '
    fout.write(output_string + '\n')
fout.close()
fin.close()
