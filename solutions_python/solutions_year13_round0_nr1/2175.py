#!/usr/bin/env python

#getting arguments
import sys
import getopt
usage = \
"""
Usage:
ttt.py -f file.inp -o file.out
"""
if len(sys.argv)<5:
    print usage
    sys.exit()

opts, args = getopt.getopt(sys.argv[1:],"f:o:h:")
for o,a in opts:
    if o == "-h":
        print usage
        sys.exit()
    elif o == "-f": f=a
    elif o == "-o": o=a
    else: print 'Invalid Option'

# OPENING INPUT

lines=[]
for line in open(f):
    line=line.rstrip()
    temp=line.split()
    lines.append(temp)


for i in lines:
    if i==[]: lines.remove(i)


# CREATING OUTPUT FILE
output=open(o,'w')


for j in range(0,int(lines[0][0])):
    matrix=[]
    output.write("Case #%d: "%(j+1))
    for i in range(1+j*4,((j+1)*4)+1):
        matrix.append(lines[i])
    matrix1=list(matrix)
    for n in range(0,4):
        a=[row[0][n] for row in matrix1] 
        b=[]
        c=a[0]+a[1]+a[2]+a[3]
        b.append(c)
        matrix.append(b)
    b=[]
    b1=[]
    c=matrix1[0][0][3]+matrix1[1][0][2]+matrix1[2][0][1]+matrix1[3][0][0]
    d=matrix1[0][0][0]+matrix1[1][0][1]+matrix1[2][0][2]+matrix1[3][0][3]
    b.append(c); b1.append(d)
    matrix.append(b); matrix.append(b1)
    
    if (['XXXT'] in matrix) == True or (['XXXX'] in matrix) == True or (['TXXX'] in matrix) == True or (['XTXX'] in matrix) == True or (['XXTX'] in matrix) == True: 
        output.write("X won\n")

    elif (['OOOT'] in matrix) == True or (['OOOO'] in matrix) == True or (['TOOO'] in matrix) == True or (['OTOO'] in matrix) == True or (['OOTO'] in matrix) == True: 
        output.write("O won\n")

    else:
        f=0
        for e in range(0,10):            
            for char in matrix[e][0]:
                if char=='.': f=1
        if f==1: output.write("Game has not completed\n")
        else: output.write("Draw\n")

            
        
         




