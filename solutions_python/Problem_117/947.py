#! /usr/bin/python

import sys

def rowOK(area, rownum, height):
    #print "rowOK - %d - %d" % (rownum, height)
    # All cells in the row must be equal to or lower than the height
    for colnum in range(len(area[rownum])):
        if area[rownum][colnum] > height:
            #print "False"
            return False     
    
    #print "True"
    return True

def columnOK(area, colnum, height):
    #print "colOK - %d - %d" % (colnum, height)
    # All cells in the column must be equal to or lower than the height
    for rownum in range(len(area)):
        if area[rownum][colnum] > height:
            #print "False"
            return False     
    
    #print "True"
    return True

def canmow(area):
    # for each cell, either all other cells in the row or colum must be 
    # equal to, or lower than the cell

    for rownum in range(len(area)):
        for colnum in range(len(area[rownum])):
            #print "Cell (%d, %d) = %s" % (rownum, colnum, area[rownum][colnum])
            
            if (not rowOK(area, rownum, area[rownum][colnum])) and (not columnOK(area, colnum, area[rownum][colnum])):
                return False

    return True


with sys.stdin as inp:
    numbertestcases = int(inp.readline())

    for case in range(numbertestcases):
        #print "Test case: %d" % (case+1)
        arealine = inp.readline()[:-1].split(" ")
        #print arealine
        areaN = int(arealine[0])
        areaM = int(arealine[1])
        area = []
        for nc in range(areaN):
            nline = inp.readline()[:-1].split(" ")
            arealine = []
            for h in nline:
                arealine.append(int(h))
            area.append(arealine)
        #print area
            
        if canmow(area):
            print "Case #%d: YES" % (case+1)
        else:
            print "Case #%d: NO" % (case+1)
    

