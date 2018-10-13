# -*- coding: utf-8 -*-
def mow(board, i, sens, high) : # → list [ list [ int ] ] = mowed board
    """
    i    = indice de la colonne/rangée à tondre
    sens = 0 pour horizontal
           1 pour vertical
    high = hauteur de tondure (oui oui, tondure)
    """
def isOK(board,H,L):
    maxRangee = []
    maxColonne = []
    #for y in xrange(H):
    #    maxRangee.append(max(board[y]))
    for x in xrange(L) :
        maxColonne.append(getMaxColonne(x,board))
    for y in xrange(H):
        maxRangee.append(max(board[y]))
        for x in xrange(L):
            if board[y][x]!=min(maxRangee[y],maxColonne[x]):
                return False
    return True
def getMaxColonne(x,board):
    colonne = []
    for rangee in board :
        colonne.append(rangee[x])
    return max(colonne)
for i in xrange(int(raw_input())):
    size = raw_input().split(" ")
    H = int(size[0])
    L = int(size[1])
    board = []
    for y in range(H):
        board.append([int(x) for x in raw_input().split(" ")])
    if isOK(board, H, L) :
        print "Case #"+str(i+1)+": YES"
    else :
        print "Case #"+str(i+1)+": NO"
