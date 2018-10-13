from sys import stdin as cin, exit
from copy import deepcopy as cp

data=cin.readline

def toString(layout):
    out=''
    for row in layout:
        for col in row:
            out+=col
        out+='\n'
    return out

def works(layout, laserList):
    newlayout=cp(layout)
    for l in laserList:
        r,c=l
        if newlayout[r][c]=='-':
            col=c+1
            while col<len(newlayout[r]) and newlayout[r][col]!='#':
                if newlayout[r][col]=='.':
                    newlayout[r][col]='+'
                elif newlayout[r][col]=='-' or newlayout[r][col]=='|':
                    #it destroyed a laser
                    return False
                col+=1
            col=c-1
            while col>=0 and newlayout[r][col]!='#':
                if newlayout[r][col]=='.':
                    newlayout[r][col]='+'
                elif newlayout[r][col]=='-' or newlayout[r][col]=='|':
                    #it destroyed a laser
                    return False
                col-=1
        else:
            row=r+1
            while row<len(newlayout) and newlayout[row][c]!='#':
                if newlayout[row][c]=='.':
                    newlayout[row][c]='+'
                elif newlayout[row][c]=='-' or newlayout[row][c]=='|':
                    #it destroyed a laser
                    return False
                row+=1
            row=r-1
            while row>=0 and newlayout[row][c]!='#':
                if newlayout[row][c]=='.':
                    newlayout[row][c]='+'
                elif newlayout[row][c]=='-' or newlayout[row][c]=='|':
                    #it destroyed a laser
                    return False
                row-=1
    return toString(newlayout).count('.')==0

cases=int(data())

for case in range(1,1+cases):
    line=data().split()
    rows=int(line[0])
    cols=int(line[1])
    room=[data().strip() for r in range(rows)]
    
    lasers=[]
    possible=True
    for r in range(rows):
        for c in range(cols):
            #print(r,c)
            if room[r][c]=='-' or room[r][c]=='|':  #build a list of all lasers
                lasers.append((r,c))
            if room[r][c]=='.':                     #for each spot, quick check
                this=False
                col=c
                while col<len(room[r]) and room[r][col]!='#':
                    if room[r][col]=='-' or room[r][col]=='|':
                        this=True
                        break
                    col+=1
                #print(77)
                col=c
                while col>=0 and room[r][col]!='#':
                    if room[r][col]=='-' or room[r][col]=='|':
                        this=True
                        break
                    col-=1
                #print(84)
                row=r
                while row<len(room) and room[row][c]!='#':
                    if room[row][c]=='-' or room[row][c]=='|':
                        this=True
                        break
                    row+=1
                #print(90)
                row=r
                while row>=0 and room[row][c]!='#':
                    if room[row][c]=='-' or room[row][c]=='|':
                        this=True
                        break
                    row-=1
                possible=(possible and this)
    #print('processed')
    if not possible:
        print('Case #'+str(case)+':', 'IMPOSSIBLE')
        continue
    
    for trial in range(2**len(lasers)):
        test=[[room[r][c] for c in range(cols)] for r in range(rows)]
        for index in range(len(lasers)):
            r,c=lasers[index]
            if trial & (2**index):
                test[r][c]='|'
            else:
                test[r][c]='-'
        if works(test, lasers):
            print('Case #'+str(case)+': POSSIBLE', toString(test), end='', sep='\n')
            break;
    else:
        print('Case #'+str(case)+':', 'IMPOSSIBLE')