#Get functionality
import re
import math
import string
import fractions

#Opens input file
file=open('testin2.txt')

#Opens output file
out=open('output.txt','w')

#Reads first line, which is number of cases to follow
T = int(file.readline())
for i in range(0,T):
    line = file.readline()
    #Remove new line characters
    line = line.replace('\n','')
    info = line.split(" ")
    
    N = int(info[0])
    pd = int(info[1])
    pg = int(info[2])

    gcd1 = fractions.gcd(pd,100)
    dpos = int(pd/gcd1)
    npos = int(100/gcd1)

    poss = True

    if N < npos:
        poss = False
    if pg==100 and pd != 100:
        poss = False
    if pg==0 and pd != 0:
        poss = False

##    print(gcd1)
##    print(dpos)
##    print(npos)
##    
##    poss = False
##    for x in range(0,int(100/npos)):
##        if True:
##            break
##        n = (x+1)*npos
##        d = (x+1)*dpos
##        for y in range(0,100-npos):
##            if d + y == pg and n + y <= 100:
##                poss = True
##                break
##            if n + y > 100:
##                break
    if poss:
        answer = 'Possible'
    else:
        answer = 'Broken'
    out.write('Case #')
    out.write(str(i+1))
    out.write(': ')
    #The answer goes here
    out.write(answer)
    out.write('\n')
#Close the files
out.close()
file.close()
