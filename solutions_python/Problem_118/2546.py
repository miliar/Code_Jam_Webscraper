# -*- coding:Utf-8 -*-
import os
from sys import argv
from math import sqrt
import random
import numbers

# Google Code Jam 2013
# Fair and Square - Small Set
# coded by AiMeCee - Reunion


def main() :
    f_input=argv[1:][0]
    (base,ext)=os.path.splitext(f_input)
    f_output= base+"_solved"+ext
    read_input = open(f_input,'r')
    write_output = open(f_output,'w')
    line1 = read_input.readline()
    nb_cases = int(line1)
    for case in range (1,nb_cases+1) :
        fairSquare = 0
        readLineCase = read_input.readline()
        (a,b) = readLineCase.split()
        ls_to_ignore = []
        n=int(a)
        while n <= int(b) :
            if n in ls_to_ignore :
                n+=1
            else :
                isPalindrome=False
                if str(n) == str(n)[::-1] :
                    isPalindrome=True
                    racine=int(sqrt(n))
                    if racine == sqrt(n) and str(racine) == str(racine)[::-1] :
                        fairSquare += 1
                if n**2 <= int(b) :
                    if str(n**2) == str(n**2)[::-1] and isPalindrome and n!=1 :
                        fairSquare += 1
                    ls_to_ignore.append(n**2)
                n+=1
        msg = 'Case #'+str(case)+": "+str(fairSquare)+"\n"
        write_output.writelines(msg)
    read_input.close()
    write_output.close()
    
if __name__ == "__main__" :
    main()