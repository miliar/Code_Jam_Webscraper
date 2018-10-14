'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    moves=[]
    line= file.readline().split()
    for i in range(0,string._int(line[0])):
        move=(line[2*i+1],string._int(line[2*i+2]))
        moves.append(move)
    time=0
    opos=1
    bpos=1
    lat=0
    prev='O'
    for move in moves:
        if(move[0]=='O'):
            go=abs(move[1]-opos)
            if(prev!='O'):
                go=max(0,go-lat)
                lat=go+1
            else:
                lat+=go+1
            time+=go+1
            opos=move[1]
            prev='O'
        else:
            go=abs(move[1]-bpos)
            if(prev!='B'):
                go=max(0,go-lat)
                lat=go+1
            else:
                lat+=go+1
            time+=go+1
            bpos=move[1]
            prev='B'
    return time
    
    
    

                 

file = open('./a2.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s: %s' %((i+1), converse())

