import sys
import copy
def findsink(watershed,wmap,h,w,i,j,c):
    v=watershed[i][j]
    if(i>0):
        north=watershed[i-1][j]
    else:
        north=10001
    if(i+1<h):
        south=watershed[i+1][j]
    else:
        south=10001
    if(j>0):
        west=watershed[i][j-1]
    else:
        west=10001
    if(j+1<w):
        east=watershed[i][j+1]
    else:
        east=10001
    surround=[north,west,east,south]
    sink=min(surround)
    ind=surround.index(sink)
    ni=i
    nj=j
    if(ind==0):
        ni-=1
    if(ind==1):
        nj-=1
    if(ind==2):
        nj+=1
    if(ind==3):
        ni+=1
    if(wmap[ni][nj]!='.' and wmap[ni][nj]!='*'):
        wmap[i][j]=wmap[ni][nj]
        return wmap[i][j]
    elif(wmap[ni][nj]=='*'):
        wmap[ni][nj]=wmap[i][j]=c.pop(0)
        return wmap[i][j]
    else:
        wmap[i][j]=findsink(watershed,wmap,h,w,ni,nj,c)
        return wmap[i][j]
    
    
    
def process(watershed,wmap,h,w):
    c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(h):
        for j in range(w):
            v=watershed[i][j]
            if(i>0):
                north=watershed[i-1][j]
            else:
                north=10001
            if(i+1<h):
                south=watershed[i+1][j]
            else:
                south=10001
            if(j>0):
                west=watershed[i][j-1]
            else:
                west=10001
            if(j+1<w):
                east=watershed[i][j+1]
            else:
                east=10001
            if(v<=north and v<=south and v<=west and v<=east):
                wmap[i][j]='*'
    for i in range(h):
        for j in range(w):
            if(wmap[i][j]=='*'):
                wmap[i][j]=c.pop(0)
            elif(wmap[i][j]=='.'):
                wmap[i][j]=findsink(watershed,wmap,h,w,i,j,c)
            
        
    
sys.stdin = open('B-large.in','r')
output=open('output.txt',mode='w')
n=int(input())
for i in range(n):
    watershed=[]
    waterlabel=[]
    wmap=[]
    h,w = [int(i) for i in input().split()]
    for k in range(w):
        waterlabel.append('.')
    for j in range(h):
        row = [int(i) for i in input().split()]
        watershed.append(row)
        wmap.append(copy.deepcopy(waterlabel))
    process(watershed,wmap,h,w)
    print("Case #",i+1,":",sep='',file=output)
    for i in range(h):
        for j in range(w):
            print(wmap[i][j],' ',end='',file=output)
        print(file=output)
            
            
            
