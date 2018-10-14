from io import *

def runFile(file):
    f = open(file)
    g = open("output"+file,'w')
    num = int(f.readline().rstrip('\n'))
    for i in range(num):
        xcounter = [0,0,0,0,0,0]
        ocounter = [0,0,0,0,0,0]
        xwin = False
        ywin = False
        blank = False
        for j in range(5):
            line = f.readline().rstrip('\n')
            rowx = 0
            rowo = 0
            if(j != 4):
                for k in range(4):
                    if line[k] == 'X':
                        rowx += 1
                        xcounter[k] += 1
                        if (k ==j):
                            xcounter[4] += 1
                        if(k+j == 3):
                            xcounter[5] += 1
                    elif line[k] == 'O':
                        rowo += 1
                        ocounter[k] += 1
                        if (k ==j):
                            ocounter[4] += 1
                        if(k+j == 3):
                            ocounter[5] += 1
                    elif line[k] == 'T':
                        rowx += 1
                        rowo += 1
                        ocounter[k] += 1
                        xcounter[k] +=1
                        if (k ==j):
                            ocounter[4] += 1
                            xcounter[4] += 1
                        if(k+j == 3):
                            ocounter[5] += 1
                            xcounter[5] += 1
                    elif line[k] == '.':
                        blank = True
            if(rowx == 4):
                  xwin = True
            if(rowo > 3):
                  ywin = True
        for j in xcounter:
            if j > 3:
                xwin = True
        for j in ocounter:
            if j > 3:
                ywin = True
        if((ywin and xwin) or not(xwin or ywin or blank)):
            g.write("Case #" + str(i+1) + ": Draw\n")
        elif xwin:
            g.write("Case #" + str(i+1) + ": X won\n")
        elif ywin:
            g.write("Case #" + str(i+1) + ": O won\n")
        else:
            g.write("Case #" + str(i+1) + ": Game has not completed\n")
                        
            
