'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    numbers=file.readline().split()
    size=map(int,numbers)
    array=[['.' for i in range(size[1])] for j in range(size[0])]
    for row in range(size[0]):
        line =file.readline()
        for col in range(size[1]):
            if (line[col]=='#'):
                array[row][col]='#'
    
    for row in range(size[0]):
        for col in range(size[1]):
            if (array[row][col]=='#'):
                array[row][col]='/'
                if((row==size[0]-1) or (col==size[1]-1)):
                    print "Impossible"
                    return
                if(not((array[row+1][col]=='#') and (array[row][col+1]=='#') and (array[row+1][col+1]=='#'))):
                    print "Impossible"
                    return
                array[row+1][col]='\\'
                array[row][col+1]='\\'
                array[row+1][col+1]='/'
    for row in range(size[0]):
        line=""
        for col in range(size[1]):
            line+=array[row][col]
        print line
    

                 

file = open('./a2.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s:' %((i+1))
    converse()

