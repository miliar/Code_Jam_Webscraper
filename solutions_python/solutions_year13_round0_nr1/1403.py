# Tic-Tac-Toe-Tomek

import sys

def testLigneX(tab,i):
    for j in range(4):
        if tab[i][j] in ('O','.'):
            return False
    return True

def testLigneO(tab,i):
    for j in range(4):
        if tab[i][j] in ('X','.'):
            return False
    return True

def testColonneX(tab,j):
    for i in range(4):
        if tab[i][j] in ('O','.'):
            return False
    return True

def testColonneO(tab,j):
    for i in range(4):
        if tab[i][j] in ('X','.'):
            return False
    return True

def testDiag1X(tab):
    for i in range(4):
        if tab[i][i] in ('O','.'):
            return False
    return True

def testDiag1O(tab):
    for i in range(4):
        if tab[i][i] in ('X','.'):
            return False
    return True

def testDiag2X(tab):
    for i in range(4):
        if tab[i][3-i] in ('O','.'):
            return False
    return True

def testDiag2O(tab):
    for i in range(4):
        if tab[i][3-i] in ('X','.'):
            return False
    return True

def filled(tab):
    return sum([1 for i in range(4) for j in range(4) if tab[i][j] == '.']) == 0


def testGlobal(tab):
    for i in range(4):
        if testLigneX(tab,i) or testColonneX(tab,i):
            return 'X won'
        if testLigneO(tab,i) or testColonneO(tab,i):
            return 'O won'
    if testDiag1X(tab) or testDiag2X(tab):
        return 'X won'
    if testDiag1O(tab) or testDiag2O(tab):
        return 'O won'
    if filled(tab):
        return 'Draw'
    else:
        return 'Game has not completed'

f = open('A-large.in','r')

n = int(f.readline())

output = open('A-large.out','w')

for i in range(n):
    tab = []
    for j in range(4):
        tab.append(list(f.readline()[:4]))
        #print(tab)
    output.write('Case #{}: {}\n'.format(i+1,testGlobal(tab)))
    garb = f.readline()

output.close()
f.close()
