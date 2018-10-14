#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
import numpy as np

            
# Входной файл
if len(sys.argv) < 2:
    sInputFileName = 'B-small.in'
    #sys.exit()
else:
    sInputFileName = sys.argv[1]
print sInputFileName
# Выходной файл
sOutputFileName = os.path.splitext( sInputFileName )[0]+'.out'
print sOutputFileName
InDataFile = open( sInputFileName )
OutDataFile = open( sOutputFileName, 'wt' )

NumCases = int(InDataFile.readline().rstrip())
for case in range(NumCases):
    H, W = map(int, InDataFile.readline().rstrip().split(' '))
#    print H, W
    alt = np.array([], dtype=np.int16)
    arr = np.zeros((H,W),dtype=np.int16)
    ach = np.zeros((H,W),dtype=np.character)
 #   print ach
    for row in range(H):
        t = np.array(map(int, InDataFile.readline().rstrip().split(' ')), dtype = np.int16)
        alt = np.concatenate((alt, t), axis =0)
    alt = np.reshape(alt, (H,W))

    # обход всего массива
    CurrentCh = 'a'
    for row in range(H):
        for col in range(W):
            # вычисляем путь до падения
            fallpath = []
            addpath = (row,col)
            if alt[row][col]!= 0:
                trow, tcol = row, col
                nextrow, nextcol = row, col
                while addpath:
                    nextrow, nextcol = trow, tcol
                    if ach[nextrow][nextcol] != '':
                        for trow, tcol in fallpath:
                            ach[trow][tcol] = ach[nextrow][nextcol]
                        break
                    fallpath.append(addpath)
                    find = False
                    # Ищем минимальный в окружении
                    altmin = alt[trow][tcol]
                    if ((trow-1)>=0) and (alt[trow-1][tcol]<altmin):
                        altmin = alt[trow-1][tcol]
                        nextrow, nextcol = trow-1, tcol
                        find = True
                    if ((tcol-1)>=0) and (alt[trow][tcol-1]<altmin):
                        altmin = alt[trow][tcol-1]
                        nextrow, nextcol = trow, tcol-1
                        find = True
                    if ((tcol+1)<W) and (alt[trow][tcol+1]<altmin):
                        altmin = alt[trow][tcol+1]
                        nextrow, nextcol = trow, tcol+1
                        find = True
                    if ((trow+1)<H) and (alt[trow+1][tcol]<altmin):
                        altmin = alt[trow+1][tcol]
                        nextrow, nextcol = trow+1, tcol
                        find = True
                    if find:
                        addpath = (nextrow, nextcol)
                        trow, tcol = nextrow, nextcol
                    else:
                        addpath = []
                else:
                    for trow, tcol in fallpath:
                        ach[trow][tcol] = CurrentCh
                    CurrentCh = chr(ord(CurrentCh)+1)
                    
             #   print fallpath
#    print alt
    #print ach
    print 'Case #%d:' % (case+1)
    OutDataFile.write('Case #%d:\n' % (case+1))
    for trow in range(H):
        outstr = ''
        for tcol in range(W):
            outstr = outstr + ' '+ ach[trow][tcol]
        #print outstr.lstrip()
        outstr += '\n'
        OutDataFile.write(outstr.lstrip())
    #print 'Case #%d: %d' % (tMess+1,Num)
    #OutDataFile.write('Case #%d: %d\n' % (tMess+1,Num))
OutDataFile.close()    
InDataFile.close()

