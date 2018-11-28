# Google Code Jam Elimination Round


#class Win:
    #if charlist[0]=charlist[0]=charlist[0]=charlist[0]

def main():
    infile = open("A-large.in", 'r')
    firstline = infile.readline()
    num = int(firstline)
    f = open('output', 'w')
    countgame=1
    for game in range(num):
        gameover=False
        while (not gameover):
            position=[]
            for line in range(4):
                line=infile.readline().rstrip()
                position.append(line)
            
        # Split each character
            charlist=[]
            for str in position:
                firstrow = str[0]
                if firstrow=='X' or firstrow=='O':
                    numOccur=str.count(firstrow)
                    if numOccur==4:
                        print "Case #%d:" %countgame,firstrow,"won"
                        gameover=True
                        break
                    elif numOccur==3:
                        if str.count('T')==1:

                            print "Case #%d:" %countgame,firstrow,"won"
                            gameover=True
                            break
                elif firstrow=="T":
                    if str.count("X")==3:
                        print "Case #%d:" %countgame,"X won"
                        gameover=True
                        break
                    elif str.count("O")==3:
                        print "Case #%d:" %countgame,"O won"
                        gameover=True
                        break
            if not gameover: 
                for str in position:
                    for chr in list(str):
                        charlist.append(chr)
                numberempty=charlist.count(".")
# Check column now
                column=[]
                for i in range(4):
                    column.append(charlist[0+i]+charlist[4+i]+charlist[8+i]+charlist[12+i])
                for str in column:
                    firstcol = str[0]
                    if firstcol=='X' or firstcol=='O':
                        numOccur=str.count(firstcol)
                        if numOccur==4:
                            print "Case #%d:" %countgame,firstcol,"won"
                            gameover=True
                            break
                        elif numOccur==3:
                            if str.count('T')==1:
                                print "Case #%d:" %countgame,firstcol,"won"
                                gameover=True
                                break
                    elif firstcol=="T":
                        if str.count("X")==3:
                            print "Case #%d:" %countgame,"X won"
                            gameover=True
                            break
                        elif str.count("O")==3:
                            print "Case #%d:" %countgame,"O won"
                            gameover=True
                            break
            if not gameover:
# Check diagonal
                diagonal=[]
                
                diagonal.append(charlist[0]+charlist[5]+charlist[10]+charlist[15])
                diagonal.append(charlist[3]+charlist[6]+charlist[9]+charlist[12])
                for str in diagonal:
                    firstdia = str[0]
                    if firstdia=='X' or firstdia=='O':
                        numOccur=str.count(firstdia)
                        if numOccur==4:
                            print "Case #%d:" %countgame,firstdia,"won"
                            gameover=True
                            break
                        elif numOccur==3:
                            if str.count('T')==1:
                                print "Case #%d:" %countgame,firstdia,"won"
                                gameover=True
                                break
                    elif firstdia=="T":
                        if str.count("X")==3:
                            print "Case #%d:" %countgame,"X won"
                            gameover=True
                            break
                        elif str.count("O")==3:
                            print "Case #%d:" %countgame,"O won"
                            gameover=True
                            break
            if not gameover:
                if numberempty==0:
                    print "Case #%d:"%countgame,"Draw"
                else:
                    print "Case #%d:"%countgame,"Game has not completed"
            gameover=True
            infile.readline()
            countgame+=1

main()