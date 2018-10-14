'''
Created on 2011/5/22

@author: bletchley
'''

filename = "../A-large.in"
file=open(filename)

taskN = int(file.readline())
for T in range(1,taskN+1):
    string = file.readline()
#    print string
    tok=string.split(" ")
    row = int(tok[0])
    col = int(tok[1])
    map = {}
#    print row ,col
    for i in range(0,row):
        map[i]={}
        string = file.readline()
#        print string,col
        for j in range(0,col):
            map[i][j]=string[j]
    
    for i in range(0,row-1):
        for j in range(0,col-1):
            if map[i][j]=='#' and map[i+1][j]=='#' and map[i][j+1]=='#' and map[i+1][j+1]=='#':
                map[i][j] = '/'
                map[i+1][j]='\\'
                map[i][j+1]='\\'
                map[i+1][j+1]='/'
    good = 1
    for i in range(0,row):  
        str =""
        for j in range(0,col):
            if map[i][j]=='#':
                 good =0 
    
    print "Case #%d: "%(T)
    if good == 0:
        print "Impossible"
        continue
    for i in range(0,row):  
        str =""
        for j in range(0,col):
            str += map[i][j]
        print str