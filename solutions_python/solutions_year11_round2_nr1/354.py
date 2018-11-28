#Get functionality
import re
import math
import string
import fractions

#Opens input file
file=open('testin6.txt')

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
    wins = []
    wp = []
    owp = []
    oowp = []
    games = []
    record = []
    out.write('Case #')
    out.write(str(i+1))
    out.write(': \n')
    for j in range(0,N):
        line = file.readline()
        line = line.replace('\n','')
        record.append(line)
        wincount = 0
        gamecount = 0
        for l in line:
            if l=='1':
                wincount+=1
                gamecount+=1
            elif l=='0':
                gamecount+=1
        wins.append(wincount)
        games.append(gamecount)
        wp.append(wincount/gamecount)
    for j in range(0,N):
        owpsum = 0
        owpcount = 0
        for k in range(0,N):
            if j!=k:
                if record[k][j]=='.':
                    pass
                elif games[k]-1!=0:
                    if record[k][j]=='1': 
                        owpsum+=((wins[k]-1)/(games[k]-1))
                        owpcount+=1
                    elif record[k][j]=='0':
                        owpsum+=((wins[k])/(games[k]-1))
                        owpcount+=1
        owp.append(owpsum/owpcount)
    for j in range(0,N):
        oowpsum = 0
        oowpcount = 0
        for k in range(0,N):
            if j!=k:
                if record[j][k]!='.':
                    oowpsum+=owp[k]
                    oowpcount+=1
        oowp.append(oowpsum/oowpcount)
    for j in range(0,N):
        rpi = (.25*wp[j]) + (.5*owp[j]) + (.25*oowp[j])
        out.write(str(rpi))
        out.write('\n')
    
    
#Close the files
out.close()
file.close()
