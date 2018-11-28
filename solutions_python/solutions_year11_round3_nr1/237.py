'''
Created on May 22, 2011

@author: diego
'''

import sys

def check(mat,x,y):
    if(len(mat[x])<=y+1):
        return False
    if(len(mat)<=x+1):
        return False
    
    
    if(mat[x][y]!="#"):
        return False
    if(mat[x+1][y]!="#"):
        return False
    if(mat[x][y+1]!="#"):
        return False
    if(mat[x+1][y+1]!="#"):
        return False
    return True

def paint(mat,x,y):
    mat[x][y]="/"
    mat[x+1][y]="\\"
    mat[x][y+1]="\\"
    mat[x+1][y+1]="/"
    return mat
def solve(mat,rows,cols):

    
    for x in range(0,rows-1):
        for y in range(0,cols-1):
            if mat[x][y]=="#":
                if(check(mat,x,y)):
                    mat=paint(mat,x,y)
                else:
                    return "Impossible"
                
    for row in mat:
        if "#" in row:
            return "Impossible" 
    
    return mat

if __name__ == '__main__':
    file=open('test.dat')
    lines=file.readlines()
    testCases=int(lines[0])
    lines=lines[1:]
    i=1
    while(len(lines)>0):
        mat=[]
        line=lines[0]
        line=line.split()
        rows=int(line[0])
        cols=int(line[1])
        lines=lines[1:]
        for x in range(0,rows):
            line=lines[x]
            line=line.replace("\n","")
            row=list(line)
            mat+=[row]
        
        resp=solve(mat,rows,cols)
        print 'Case #' + str(i) + ':'
        if(resp=="Impossible"):
            print resp
        else:
            for row in resp:
                for c in row:
                    sys.stdout.write(c)
                print ""
            
        if(rows!=1):
            lines=lines[rows:]
        else:
            lines=lines[1:]
        i=i+1
        
        