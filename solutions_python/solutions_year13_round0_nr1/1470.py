# -*- coding: utf-8 -*-

def old_inputToOutput(inpute) :
    mi = inpute.index("\n")
    m = inpute[:mi]
    inpute = inpute[mi:].split("\n\n")
    i = 1
    for el in inpute :
        el = el.replace("\n","")
        print "Case #"+str(i),":",isVictory(el)
        i+=1
def isVictory(intro, board): # → str
    """
    True : partie finie, égalité
    False: partie en cours
    O    : O gagne
    X    : X gagne
    """
    victory = False
    directions = [[0,1], [4,1], [8,1], [12,1],
                  [0,4], [1,4], [2,4], [3,4],
                  [0,5], [3,3]]
    i = 0
    while (not victory) and (i<10) :
        # tant qu'on a pas trouvé une ligne gagnate
        # on balaye toutes les lignes
        coord, speed = directions[i][0], directions[i][1]
        side = board[coord]
        if side!='.' :
            j=0
            victory = True
            if side=='T' :
                if board[coord+speed]!='.':
                    j+=1
                    coord+=speed
                    side = board[coord]
                else :
                    victory = False
            else :
                if side=="." :
                    print "TTTTTTTTTT NUUUUUUUUUULLL"
            while (j<4) and (victory==True) :
                # on balaye la ligne, tant que c'est bon, on regarde la suite
                # dès qu'on voit que la ligne ne peut gagner,  on quitte
                victory= victory and (board[coord] in side+"T")
                coord+=speed
                j+=1
        i+=1
    if victory :
        return intro+" "+side+" won"
    if board.count('.')==0 :
        return intro+" Draw"
    return intro+" Game has not completed"

n = int(raw_input())
texte = ""
for i in xrange(n):
    board = ""
    for j in xrange(4):
        board+=raw_input()
    texte+=isVictory("Case #"+str(i+1)+":", board)+"\n"
    raw_input()
print texte[:-1]
