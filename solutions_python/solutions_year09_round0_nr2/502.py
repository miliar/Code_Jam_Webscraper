import sys
import string
import operator
import math
import re

# globals
infile = ''
N = 0
output = []
debug = False
dict=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def processCase(iCase):
    global infile, currentLine, debug
    if debug:
        print '### processing case '+str(iCase+1)
    
    # read data
    [H,W] = map(int,infile[currentLine].split())
    currentLine += 1
    mat=[]
    for i in range(H):
        mat.append(map(int,infile[currentLine].split()))
        currentLine += 1
    if debug:
        print mat
    
    ## solve the problem
    ## chart the map
    # find the first unprocessed point and find it's neighboring points
    # until no point left
    nPoint = H*W
    currLabel = 1;
    chart = array2d(H,W)
    direction = array2d(H,W)
    computeDirection(mat, direction,H,W)
    while True:
        lowXY = findLowest(mat,chart,H,W)
        if lowXY == []:
            break
        chart[lowXY[0]][lowXY[1]]=currLabel
        processNeighbor(mat,chart,direction,currLabel,H,W,lowXY[0],lowXY[1])
        currLabel += 1
    ## convert the chart to letters
    chart2Letter(chart, H,W)
    
    return chart2string(chart,H,W) 

def chart2string(chart ,H,W):
    s=''
    for i in range(H):
        for j in range(W):
            s += chart[i][j]+' '
        s+='\n'
    return s


def chart2Letter(chart, H,W):
    global dict
    k = 0
    m = {}
    for i in range(H):
        for j in range(W):
            if not chart[i][j] in m:
                m[chart[i][j]]=k
                k+=1
    for i in range(H):
        for j in range(W):
            chart[i][j] = dict[m[chart[i][j]]]
    return


def findLowest(mat, chart, H,W):
    lowXY=[]
    lowest = 1000000
    for i in range(H):
        for j in range(W):
            if chart[i][j]==0 and isLocalLowest(mat,i,j,H,W) and mat[i][j]<lowest:
                lowXY = [i,j]
                lowest = mat[i][j]
    return lowXY


def isLocalLowest(mat, x,y,H,W):
    if x+1<H and mat[x+1][y]<mat[x][y]:
        return False
    elif x-1>=0 and mat[x-1][y]<mat[x][y]:
        return False
    elif y+1<W and mat[x][y+1]<mat[x][y]:
        return False
    elif y-1>=0 and mat[x][y-1]<mat[x][y]:
        return False
    return True
    

# compute flow direction: stay:0, North-1, West-2, East-3, South-4
def computeDirection(mat, direction, H,W):
    for i in range(H):
        for j in range(W):
            lowest = 1000
            direction[i][j]=0
            if i-1>=0 and mat[i-1][j]<lowest and mat[i-1][j]<mat[i][j]:#up
                direction[i][j]=1
                lowest = mat[i-1][j]
            if j-1>=0 and mat[i][j-1]<lowest and mat[i][j-1]<mat[i][j]:#west
                direction[i][j]=2
                lowest = mat[i][j-1]
            if j+1<W and mat[i][j+1]<lowest and mat[i][j+1]<mat[i][j]:#east
                direction[i][j]=3
                lowest = mat[i][j+1]
            if i+1<H and mat[i+1][j]<lowest and mat[i+1][j]<mat[i][j]:#south
                direction[i][j]=4
                lowest = mat[i+1][j]
    return
                

# if neighbor flows into this cell, then mark with the same label
def processNeighbor(mat, chart, direction, currLabel, H, W, x, y):
    if x-1>=0 and chart[x-1][y]==0 and direction[x-1][y]==4:
        chart[x-1][y] = currLabel
        processNeighbor(mat, chart, direction, currLabel,H,W,x-1,y)
    if y-1>=0 and chart[x][y-1]==0 and direction[x][y-1]==3:
        chart[x][y-1] = currLabel
        processNeighbor(mat, chart, direction, currLabel,H,W,x,y-1)
    if x+1<H and chart[x+1][y]==0 and direction[x+1][y]==1:
        chart[x+1][y] = currLabel
        processNeighbor(mat, chart, direction, currLabel,H,W,x+1,y)
    if y+1<W and chart[x][y+1]==0 and direction[x][y+1]==2:
        chart[x][y+1] = currLabel
        processNeighbor(mat, chart, direction, currLabel,H,W,x,y+1)
    return



def array2d(nRow, nCol):
    mat = []
    for i in range(nRow):
        row = [0]*nCol
        mat.append(row)
    return mat



# apply a function to a list
def map( fun, list ):
    nlist = []
    for item in list:
        nlist.append( fun( item ) )
    return nlist

    
# Main procedure
infileName = sys.argv[1]
infile = open(infileName, 'r').readlines()
N=int(infile[0])
currentLine = 1

output = []
for i in range(N):
    result = processCase(i)
    output.append(result)
    
for i,v in enumerate(output):
    print 'Case #'+str(i+1)+':\n',v,
    