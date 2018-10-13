import os
import sys

#fname = 'sample'
fname = 'D-small-attempt0'
with open(fname+'.in') as f:
    lines = f.readlines()

T = int(lines[0].replace('\n',''))

t = 1

outfile = open(fname+'.out','w')

def getWinner(X,R,C):
    if R*C%X!=0:
        return "RICHARD"

    if X<3:
        return "GABRIEL"

    if X==3:
        if R*C>3:
            return "GABRIEL"
        else:
            return "RICHARD"

    if X==4:
        if R*C>11:
            return "GABRIEL"
        else:
            return "RICHARD"

while t<=T:
    line = lines[t]
    line = line.split(' ')
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])

    winner = getWinner(X,R,C)

    #print("""Case #%s: %s\n""" %(t,winner))
    outfile.write("""Case #%s: %s\n""" %(t,winner))
    t+=1

outfile.close()
