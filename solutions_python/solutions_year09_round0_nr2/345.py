#Python 2.6 on Windows XP
#Jonathan Hsu
#Google Code Jam 2009

#Watersheds

import re
import glob
import os
import string

mat=[]
matmap=[]
w=-1
h=-1
letter=0
def proc(y,x):
    global mat,matmap,w,h,letter
    maxval=mat[y][x]
    maxpos=[y,x]

    if(matmap[y][x]!=None):
        return matmap[y][x]
    
    if(y-1>=0 and mat[y-1][x]<maxval):
        maxval=mat[y-1][x]
        maxpos=[y-1,x]
    if(x-1>=0 and mat[y][x-1]<maxval):
        maxval=mat[y][x-1]
        maxpos=[y,x-1]
    if(x+1<w and mat[y][x+1]<maxval):
        maxval=mat[y][x+1]
        maxpos=[y,x+1]
    if(y+1<h and mat[y+1][x]<maxval):
        maxval=mat[y+1][x]
        maxpos=[y+1,x]

    if(maxval==mat[y][x]):
        matmap[y][x]=string.lowercase[letter]
        letter=letter+1
        return matmap[y][x]
    else:
        a=proc(*maxpos)
        matmap[y][x]=a
        return a
    

#def flow(mat):

for filename in glob.glob("*.in"):
    outfile=filename.replace(".in",".out")
    if(os.path.exists(outfile)):
        continue
    f=open(filename)
    ff=open(outfile,"w+")

    t=int(f.readline())
    s=""

    ans=[]

    for iii in range(t):
        h,w=[int(i) for i in f.readline().split()]
        mat=[[int(i) for i in f.readline().split()] for j in range(h)]
        matmap=[[None]*w for i in range(h)]
        letter=0
        for y,v in enumerate(mat):
            for x,vv in enumerate(v):
                proc(y,x)
        ans.append("Case #%d:\r\n"%(iii+1)+"\r\n".join([" ".join(i) for i in matmap]))

    ff.write("\r\n".join(ans))
    
    ff.flush()
    ff.close()
    f.flush()
    f.close()
