#!/usr/bin/python

import fileinput 

debug_mode=False
def intersect(a, b):
     return list(set(a) & set(b))
def dprint(s):
    if debug_mode==True:
        print(s)
fi=fileinput.input()
nTestCases=int(fi.readline())
def print_result(result):
    if result==None:
        print("Impossible")
    else:
        for line in result:
            l=""
            for element in line:
                l+=element
            print("%s"%l)
def revert(grid):
    if(debug_mode):
        dprint("Before revert:")
        print_result(grid)
    res=[]
    lines=len(grid[0])
    columns=len(grid)
    dprint("lines: %d"%lines)
    for i in xrange(0,lines):
        res.append([])
        for j in xrange(0,columns):
            res[i].append([])
    for i in xrange(0,lines):
        for j in xrange(0,columns):
            x=grid[j][i]
            res[i][j]=x
    if(debug_mode): 
        dprint("After revert:")
        print_result(res)
    return res

for testNumber in range(1, nTestCases+1):
    dprint("start case..")
    rcm= map(int,fi.readline().strip().split(" "))
    r, c, m = rcm[0],rcm[1],rcm[2]
    dprint("%d %d %d"%(r,c,m))
    result=[]
    if r > c:
        r,c=c,r
        inverted=True
        dprint("Inverted")
    else:
        inverted=False
    for i in xrange(0,r):
        result.append([])
        for j in xrange(0,c):
            result[i].append('.')
    if r==1:
        for i in xrange(0,m):
            result[0][i]='*'
    elif r==2:
        if m==2*c-1:
            for i in xrange(0,c):
                result[0][i]='*'
                result[1][i]='*'
        elif (c>2 and (m%2 == 0) and m/2 <= c-2 ):
            for i in xrange(0,m/2):
                result[0][i]='*'
                result[1][i]='*'
        elif(c==2):
            if (m==0):
                result=[['.','.'],['.','.']]
            elif (m == 3):
                result=[['*','*'],['*','*']]
            else:
                result=None
        else:
            result=None
    else:
        remaining=r*c-m
        dprint("remaining: %d"%remaining)
        if remaining==1:
            for i in xrange(0,r):
                for j in xrange(0,c):
                    result[i][j]='*'
        elif remaining in (2,3,5,7):
            result=None
        else:
            if m <= (r-3)*c:
                dprint("tata")
                mcount=m
                for i in xrange(0,r):
                    for j in xrange(0,c):
                        if mcount>1:
                            result[r-1-i][j]='*'
                        elif mcount==1:
                            result[r-1-i][j]='*'
                            maxi=i
                            maxj=j
                        mcount-=1
                if c-m%c==1:
                    dprint("toto")
                    dprint(maxi)
                    dprint(maxj)
                    if (maxi !=0 or maxj !=0):
                        result[r-1-maxi][maxj]='.'
                        result[r-1-(maxi+1)][0]='*'
            else:
                for i in xrange(0,r-3):
                    for j in xrange(0,c):
                        result[r-1-i][j]='*'
                m-=c*(r-3)
                dprint("m: %d"%m)
                if m%3==0:
                    for i in xrange(0,m/3):
                        result[0][i]='*'
                        result[1][i]='*'
                        result[2][i]='*'
                elif m%3==1:
                    for i in xrange(0,m/3):
                        result[0][i]='*'
                        result[1][i]='*'
                        result[2][i]='*'
                    result[2][m/3]='*'
                elif m%3==2:
                    for i in xrange(0,m/3):
                        result[0][i]='*'
                        result[1][i]='*'
                        result[2][i]='*'
                    result[2][m/3]='*'
                    result[2][m/3+1]='*'
    if result:
        result[0][c-1]='c'
    if inverted and result:
        result=revert(result)
    if debug_mode:
        print_result(result)

    
    print("Case #%d:"%testNumber)
    print_result(result)




