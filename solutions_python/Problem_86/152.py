'''
Created on 2011/5/22

@author: bletchley
'''

filename = "../C-small-attempt0.in"
file=open(filename)

taskN = int(file.readline())

for T in range(1,taskN+1):
    str = file.readline()
    tok = str.split(" ")
    N = int(tok[0])
    L = int(tok[1])
    H = int(tok[2])
    str = file.readline()
    tok = str.split(" ")
    arr = {}
    flag = 0
    min = 0;
    for i in range(0,N):
        arr[i]=int(tok[i])
    
    for j in range(L,H+1):
       hor = 1
       #print j
       for i in range(0,N):        
         if not (j % arr[i] ==0 or arr[i]%j==0) :
             hor = 0;
       if hor == 1 :
           min = j
           flag = 1
           break;
    if flag == 0:
        print "Case #%d: NO"%(T)
    else :
        print "Case #%d: %d"%(T,min)