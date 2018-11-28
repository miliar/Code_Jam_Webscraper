#!/usr/bin/python
def solveGame():
    infile=open("A-small-attempt2.in","r")
    outFile=open("A-small-attempt2.ou","w")
    numOfinp=int(infile.readline().strip('\n'))
    caseNum=1
    while caseNum<=numOfinp:
        rowsx=[]
        rowso=[]
        line=infile.readline()
        flagx=0
        flago=0
        while line!='\n':
            line=line.strip('\n')
            rowsx.append(line.replace('T','X'))
            rowso.append(line.replace('T','O'))
            line=infile.readline()
        if "XXXX" in rowsx:
            outFile.write("Case #"+str(caseNum)+": X won\n")
            flagx=1
            
        if "OOOO" in rowso:
            outFile.write("Case #"+str(caseNum)+": O won\n")
            flago=1
            
        i=0
        while i<4:
            if rowsx[0][i]==rowsx[1][i]==rowsx[2][i]==rowsx[3][i]=='X' and flagx==0:
                outFile.write("Case #"+str(caseNum)+": X won\n")
                flagx=1
                
            if rowso[0][i]==rowso[1][i]==rowso[2][i]==rowso[3][i]=='O' and flago==0:
                outFile.write("Case #"+str(caseNum)+": O won\n")
                flago=1
            i+=1
       
        if rowsx[0][0]==rowsx[1][1]==rowsx[2][2]==rowsx[3][3]=='X' or rowsx[0][3]==rowsx[1][2]==rowsx[2][1]==rowsx[3][0]=='X' and flagx==0:
            outFile.write("Case #"+str(caseNum)+": X won\n")
            flagx=1
       
        if rowso[0][0]==rowso[1][1]==rowso[2][2]==rowso[3][3]=='O' or rowso[0][3]==rowso[1][2]==rowso[2][1]==rowso[3][0]=='O' and flago==0:
            outFile.write("Case #"+str(caseNum)+": O won\n")
            flago=1

        notComplete=0
        if flagx==0 and flago==0:
            for line in rowso:
                if '.' in line:
                    outFile.write("Case #"+str(caseNum)+": Game has not completed\n")
                    notComplete=1
                    break

        if notComplete==0 and flagx==0 and flago==0:
            outFile.write("Case #"+str(caseNum)+": Draw\n")
            
        caseNum+=1

solveGame()
