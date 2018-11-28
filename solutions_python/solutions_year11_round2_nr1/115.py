'''
Created on May 20, 2011

@author: Phil
'''

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0]

inpname = raw_input("File input: ")

fr = open(inpname, 'r')
fc = fr.read()
fr.close()

output = ""

lines = fc.split('\n')

numOfCases = int(lines[0])

def wp(st):
    t = 0
    w = 0
    for c in st:
        if c=='1':
            w=w+1
            t=t+1
        if c=='0':
            t=t+1
    return [w,t]

def score(winloss, o, oo):
    return float(0.25*float(winloss[0])/float(winloss[1])+0.5*o+0.25*oo)

lindex = 1
casenum = 0
while casenum<numOfCases:
    board = []
    for z in range(int(lines[lindex])):
        board.append(lines[lindex+z+1])
    wl = []
    for games in board:
        wl.append(wp(games))
    owps = []
    for games in board:
        sumowp = 0
        cou = 0
        for i in range(len(games)):
            if games[i]!='.':
                if games[i]=='0':
                    sumowp = sumowp + float(wl[i][0]-1)/float(wl[i][1]-1)
                    cou = cou+1
                if games[i]=='1':
                    sumowp = sumowp + float(wl[i][0])/float(wl[i][1]-1)
                    cou=cou+1
        owps.append(float(sumowp/cou))
        
    oowps = []
    for games in board:
        sumoo = 0
        count = 0
        for i in range(len(games)):
            if games[i]!='.':
                sumoo = sumoo+owps[i]
                count = count+1
        oowps.append(float(sumoo/count))
    output = output + "Case #"+str(casenum+1)+":\n"
    for i in range(len(board)):
        output = output + str(score(wl[i], owps[i], oowps[i]))+"\n"
    lindex = lindex + int(lines[lindex])+1
    casenum = casenum+1




fw = open(inpname.split('.')[0] + '-out.txt', 'w')
fw.write(output)
fw.close()
