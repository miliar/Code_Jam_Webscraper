'''
Created on Apr 29, 2011

@author: vipyati
'''
from file.FileOp import *
from decimal import *
#name = 'B-large-practice'
name = 'A-small-attempt0'
f = FileRead(name)
o = FileWrite(name)


T= f.INT()
for t in range(T):
    N = f.INT()
    Ot,Op = 0,1
    Bt,Bp = 0,1
    for i in range(N):

        c = f.STR()
        p = f.INT()
        
        if c =='O':
            Ot = Ot+ abs(p-Op)+1
            if Ot<=Bt:
                Ot=Bt+1
            Op = p
        if c == 'B':
            Bt = Bt + abs(p-Bp)+1
            if Bt<=Ot:
                Bt = Ot+1
            Bp = p
        #print Ot,Bt
    o.writeCase(t+1, max(Ot,Bt))
            
    