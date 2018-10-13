'''
Created on May 7, 2011

@author: Remigijus
'''
#from encodings.punycode import digit
import re
global T,N

def modulis(x):
    if x < 0:
        return -x
    return x

inputFile = open("A-large.in", "rb")
T = inputFile.readline().split()[0]
print(T)

outputFile = open("A-large.out", "w")






for q in range(int(T)):
    line = inputFile.readline().split()
    
    O = 1
    B = 1
    Om = 0
    Bm = 0
    case = 0;
    
    for n in range(len(line[1:])):
        this = line[n]
        next = line[1+n]
        if this == 'O':
            print 'O'
            step = int(next)-O
            O += step
            Om += modulis(step)
            while(Om < Bm):
                Om += 1
            Om += 1
            
            print step, O, Om
        if this == 'B':
            print 'B'
            step = int(next)-B
            B += step
            Bm += modulis(step)
            while(Bm < Om):
                Bm += 1
            Bm += 1
            print step, B, Bm
        
    if Bm > Om:
       case = Bm
    else:
        case = Om

    print "Case #" + str(q+1) +":", case
    print >>outputFile, "Case #" + str(q+1) +":", case
     
    
    