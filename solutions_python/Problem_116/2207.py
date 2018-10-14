__author__ = 'JT Thompson'

def whowon(game, count):
    count += 1
    count = str(count)
    xwin = ["XXXX","XXXT","XXTX","XTXX","TXXX","OOOO","OOOT","OOTO","OTOO","TOOO"]

    diag1 = game[0]+game[4]+game[8]+game[12]
    diag2 = game[1]+game[5]+game[9]+game[13]
    diag3 = game[2]+game[6]+game[10]+game[14]
    diag4 = game[3]+game[7]+game[11]+game[15]
    diag5 = game[0]+game[5]+game[10]+game[15]
    diag6 = game[12]+game[9]+game[6]+game[3]

    if any(game[0:4] in s for s in xwin):
        if "X" in game[0:4]:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(game[4:8] in s for s in xwin):
        if "X" in game[4:8]:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(game[8:12] in s for s in xwin):
        if "X" in game[8:12]:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(game[12:16] in s for s in xwin):
            if "X" in game[12:16]:
                print "Case #"+count+": X won"
            else:
                print "Case #"+count+": O won"
    elif any(diag1 in s for s in xwin):
        if "X" in diag1:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(diag2 in s for s in xwin):
        if "X" in diag2:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(diag3 in s for s in xwin):
        if "X" in diag3:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(diag4 in s for s in xwin):
        if "X" in diag4:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(diag5 in s for s in xwin):
        if "X" in diag5:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif any(diag6 in s for s in xwin):
        if "X" in diag6:
            print "Case #"+count+": X won"
        else:
            print "Case #"+count+": O won"
    elif not "." in game:
        print "Case #"+count+": Draw"
    else:
        print "Case #"+count+": Game has not completed"





ins = open( "A-large.in" )
count = ins.readline()
game = ''

for j in range(int(count)):
    for i in range(4):
        game+=ins.read(5)
        game = game.rstrip('\n')
    whowon(game,j)
    game = ''
    blank = ins.readline()
ins.close()


