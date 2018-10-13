# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:06:56 2012

@author: Big one
"""
def digits(number):
    digits = []
    while number > 0:
        d = number%10
        number = (number - d)/10
        digits.append(d)
    digits.reverse()
    return digits
    
def getNumber(dig, delta):
    n = 0
    ld = len(dig)
    for i in range(ld):
        n = n*10 + dig[(i+delta)%ld]
    return n
    
    
fi = open('C-small-attempt0.in','r+')
fi.readline()
with open("Coutput.txt", "w") as fileout:
    i = 1
    for line in fi:
        line = line.replace('\n','')
        [A, B] = line.split(" ")
        A = int(A)
        B = int(B)
        suma = 0
        last = [0,0]
        for n in range(A, B):
            dig = digits(n)
            ld = len(dig)
            for d in range(1, ld):
                n2=getNumber(dig, d)
                if n2 < 10**(ld-1):
                    continue
                if n < n2 and n2 <=B:
                    #print n, n2
                    #if ld == 4:
                        #rez.append([n, n2])
                    if last[0]==n and last[1]==n2:
                        continue
                    last[0] = n
                    last[1] = n2
                    suma += 1
        print i, suma
        
        fileout.write("Case #%s: " %i)
        fileout.write('%s\n' %suma)
        i += 1
    

    
fi.close()

