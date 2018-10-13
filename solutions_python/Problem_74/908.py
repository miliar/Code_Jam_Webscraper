#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     07/05/2011
# Copyright:   (c) Dan 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

file1=r"d:\Download Firefox\A-large.in"
output=r"d:\Download Firefox\A-large.out"

def solve(nr,moves,orange,blue,k):
    io=0
    ib=0

    t=0
    i=0
    poz_o=1
    poz_b=1
    if len(orange)!=0:
        io=0
        next_o=orange[0]
    else:
        next_o=0

    if len(blue)!=0:
        next_b=blue[0]
        ib=0
    else:
        next_b=0

    while i<nr:
        c=moves[i][0]
        m=int(moves[i][1:])
        if c=='O':
            if poz_o==m:
                i=i+1
                io=io+1
                if io<=len(orange)-1:
                    next_o=orange[io]
            else:
                if poz_o<next_o:
                    poz_o=poz_o+1
                else:
                    poz_o=poz_o-1
            if next_b!=0:
                if poz_b==next_b:
                    pass
                else:
                    if poz_b<next_b:
                        poz_b=poz_b+1
                    else:
                        poz_b=poz_b-1

        if c=='B':
            if poz_b==m:
                i=i+1
                ib=ib+1
                if ib<=len(blue)-1:
                    next_b=blue[ib]
            else:
                if poz_b<next_b:
                    poz_b=poz_b+1
                else:
                    poz_b=poz_b-1
            if next_o!=0:
                if poz_o==next_o:
                    pass
                else:
                    if poz_o<next_o:
                        poz_o=poz_o+1
                    else:
                        poz_o=poz_o-1
        t=t+1
#    print(t)
    g.write('Case #%d: %d\n'% (k,t))



f=open(file1,'r')
g=open(output,'w')
aux=f.readline().rstrip('\n')
t=int(aux)
for i in range(1,t+1):
    line=f.readline().rstrip('\n')
    list=line.split(' ')
    nr=int(list[0])
    list=list[1:]
    moves=[]
    orange=[]
    blue=[]
    for j in range(len(list)):
        if j%2==1:
            moves.append(list[j-1]+list[j])
            if list[j-1]=='O':
                orange.append(int(list[j]))
            if list[j-1]=='B':
                blue.append(int(list[j]))
#    print(nr,moves,orange,blue)
    solve(nr,moves,orange,blue,i)


f.close()
g.close()


