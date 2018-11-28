#! /usr/bin/python


numinput=int(raw_input())

for linnum in range(numinput):
    lines=[]
    for ii in range(4):
        lines.append(raw_input())
    try:
        raw_input()
    except EOFError:
        pass

    def checkHorz(char):
        win=False
        for ri in range(4):
            correct=True
            for ci in range(4):
                if(lines[ri][ci]!=char and lines[ri][ci]!='T'):
                    correct=False
                    break
            if correct:
                win=True
                break
        
        return win

    def checkVert(char):
        win=False
        for ci in range(4):
            correct=True
            for ri in range(4):
                if(lines[ri][ci]!=char and lines[ri][ci]!='T'):
                    correct=False
                    break
            if correct:
                win=True
                break
        
        return win

    def checkDiag(char,up=False):
        
        i=0
        while(i<4):
            row=i
            if up:
                row=3-i
            if(lines[row][i]!= char and lines[row][i]!='T'):
                return False
            i+=1

        return True
    
    def checkAll(char):
        return checkHorz(char) or checkVert(char) or checkDiag(char) or checkDiag(char,True)

    if(checkAll('X')):
        print("Case #%s: X won"%(linnum+1));
        continue
    elif(checkAll('O')):
        print("Case #%s: O won"%(linnum+1));
        continue
    else:
        notcomplete=False
        for line in lines:
            for cell in line:
                if(cell=='.'):
                    print("Case #%s: Game has not completed"%(linnum+1))
                    notcomplete=True
                    break
            if(notcomplete):
                break
        if(notcomplete):
            continue
        print("Case #%s: Draw"%(linnum+1))

