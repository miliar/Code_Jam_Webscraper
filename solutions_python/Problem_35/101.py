'''
Created on 2009-9-3

@author: ufo
'''
import sys

def getflow(x,y):
    global h,w,altitudes,m,markindex,mark
    x1,y1=x,y
    a=altitudes[x1][y1]
    if x>0 and altitudes[x-1][y]<a:
        x1=x-1
        y1=y
        a=altitudes[x1][y1]
    if y>0 and altitudes[x][y-1]<a:
        x1=x
        y1=y-1
        a=altitudes[x1][y1]
    if y<w-1 and altitudes[x][y+1]<a:
        x1=x
        y1=y+1
        a=altitudes[x1][y1]
    if x<h-1 and altitudes[x+1][y]<a:
        x1=x+1
        y1=y
        a=altitudes[x1][y1]
    if mark[x1][y1] is None and (x1!=x or y1!=y):
        x2,y2,mark[x1][y1]=getflow(x1,y1)
    elif mark[x1][y1] is None and x1==x and y1==y:
        mark[x1][y1]=m[markindex]
        markindex=markindex+1
    return x1,y1,mark[x1][y1]
def main():
    global h,w,altitudes,m,markindex,mark

    for case in range(input()):
        h,w=map(int,raw_input().split())
        altitudes=[[None]*w]*h
        mark=[[None for i in range(w)] for j in range(h)]
        markindex=0
        for i in range(h):
            altitudes[i]=map(int,raw_input().split())
        sys.stdout.write('\nCase #%s:'% (case + 1))
        for i in range(h):
            print ''
            for j in range(w):
                if(mark[i][j] is None):
                    x,y,mark[i][j]=getflow(i,j)
                if(j<w-1):
                    sys.stdout.write('%s ' % (mark[i][j]))
                else:
                    sys.stdout.write('%s' % (mark[i][j]))

h,w=0,0
altitudes=[]
mark=[]
m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
markindex=0
main()