from __future__ import division, print_function
import string
import re

#file must end in newline

def cja(fInP="in.txt", fOutP="out.txt"):
    fIn = open(fInP, 'r')
    fOut = open(fOutP, 'w')
    N = int(fIn.readline())
    for n in range(0, N):
        nnn = fIn.readline()
        num = nnn[:len(nnn)-1]
        sumNum = 0
        p = 1
        d = {}
        strUp = []
        for letter in num:

            if letter in d:
                #dont ins
                pEquiv = d[letter]
            else:
                d[letter] = p
                pEquiv = p
                if (p == 1):
                    p=0
                elif (p==0):
                    p=2
                else:
                    p+=1
                
            
            strUp.append(pEquiv)

        it = 0
        base = len(d)
        count = len(strUp)
        if base == 1:
            base = 2
        for dec in strUp:

            sumNum += pow(base, count - it - 1)*dec
            #print (sumNum)
            it+=1
        
        #print (it, base, strUp, sumNum)
        fOut.write('Case #' + str(n+1) + ': ' + str(sumNum) + '\n')
