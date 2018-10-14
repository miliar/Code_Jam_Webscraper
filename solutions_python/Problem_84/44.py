# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:07:30 2011

@author: Shahar
"""

import operator as op

def printwrite(fout, text) :
    print text
    fout.write(text + '\n')
    
def Blue(tile) :
    return tile == '#'
    
def A(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Line = map(int, fin.readline().strip('\n').split(' '))
        Rows = Line[0]
        Columns = Line[1]
        Rect = []
        for iR in xrange(Rows) :
            Rect.append(list(fin.readline().strip('\n')))
        Impossible = False
        NewRect = Rect
        for iR in xrange(0,Rows-1) :
            for iC in xrange(0,Columns-1) :
                if Blue(NewRect[iR][iC]):
                    if Blue(NewRect[iR][iC+1]) and Blue(NewRect[iR+1][iC]) and \
                    Blue(NewRect[iR+1][iC+1]) :
                        NewRect[iR][iC] = '/'
                        NewRect[iR][iC+1] = '\\'
                        NewRect[iR+1][iC] = '\\'
                        NewRect[iR+1][iC+1] = '/'
                    else :
                        Impossible = True
                        break
            if Blue(NewRect[iR][Columns-1]) :
                Impossible = True
            if Impossible :
                break
        for iC in xrange(Columns) :
            if Blue(NewRect[Rows-1][iC]):
                Impossible = True
                break

        printwrite(fout, 'Case #' + str(iCNT+1) + ': ')
        if Impossible :
            printwrite(fout, 'Impossible')
        else :
            for iR in xrange(Rows) :
                printwrite(fout, reduce(op.add, NewRect[iR]))
            

if __name__ == "__main__":
    #A(sys.argv[1]);
    #A('..\\test\\A-test.in');
    #A('..\\test\\A-small-attempt0.in');
    #A('..\\test\\A-small-attempt1.in');
    A('..\\test\\A-large.in');
