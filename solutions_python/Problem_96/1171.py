'''Apr 14, 2012 Autor: Artur'''
# -*- coding: utf-8 -*-
file_in = open("B-large.in", "r")
file_out = open("B-large.out", "w")

def hinded(skoor):
    x = skoor//3
    erinevus = skoor%3
    if erinevus == 0:
        return([x, x, x])
    elif erinevus == 1:
        return([x, x, x+1])
    else:
        return[x, x+1, x+1]
def üllatavhinne(skoor):
    erinevus = skoor%3
    x = hinded(skoor)
    if skoor == 0:
        return [0, 0, 0]
    if skoor == 1:
        return [0, 0, 1]
    if skoor == 2:
        return [0, 0, 2]
    if erinevus == 0:
        x[0] -= 1
        x[2] += 1
    elif erinevus == 1:
        x[0] -= 1
        x[1] += 1
    elif erinevus==2:
        x[1] += 1
        x[2] -= 1
    return(x)
        
for case, rida in enumerate(file_in):
    if case==0:
        mitu=int(rida)
    else:
        Scores=[]
        vastus=0
        file_out.write("Case #" + str(case) + ": ")
        tükid = rida.strip().split(" ")
        N = int(tükid[0])        #Mitu osalejat
        S = int(tükid[1])        #Üllatavad skoorid 
        P = int(tükid[2])        #Kellel on suurem võrdne sellest
        for punktid in tükid[3:]:
            Scores.append(int(punktid))
        Scores.sort()
        Scores.reverse()
        
        for punktid in Scores:
            if max(hinded(punktid)) >= P:
                vastus+=1
            else:
                if S > 0:
                    if max(üllatavhinne(punktid))>=P:
                        vastus+=1
                        S-=1
        if case!=mitu:
            file_out.write(str(vastus) + "\n")
        else:
            file_out.write(str(vastus))