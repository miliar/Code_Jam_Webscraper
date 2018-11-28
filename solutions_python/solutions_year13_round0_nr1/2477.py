'''
Created on 8 avr. 2013

@author: root
'''

def readtable(incl):
    Xa=0
    Xb=0
    Xc=0
    Xd=0
    Xe=0
    Xf=0
    Xg=0
    Xh=0
    Oa=0
    Ob=0
    Oc=0
    Od=0
    Of=0
    Oe=0
    Og=0
    Oh=0
    XD1=0
    XD2=0
    OD1=0
    OD2=0
    line1=fichier.readline().rstrip('\n\r')
    line2=fichier.readline().rstrip('\n\r')
    line3=fichier.readline().rstrip('\n\r')
    line4=fichier.readline().rstrip('\n\r')

    tour=incl+1

#Lignes X
    j = 0
    while j != 4:
        if (line1[j] == "X") or (line1[j] == "T"):
            Xa += 1
        j += 1
    j = 0
    while j != 4:
        if (line2[j] == "X") or (line2[j] == "T"):
            Xb += 1
        j += 1
    j = 0        
    while j != 4:
        if (line3[j] == "X") or (line3[j] == "T"):
            Xc += 1
        j += 1
    j = 0        
    while j != 4:
        if (line4[j] == "X") or (line4[j] == "T"):
            Xd += 1
        j += 1
   #Lignes O 
    j = 0
    while j != 4:
        if (line1[j] == "O") or (line1[j] == "T"):
            Oa += 1
        j += 1
    j = 0
    while j != 4:
        if (line2[j] == "O") or (line2[j] == "T"):
            Ob += 1
        j += 1
    j = 0        
    while j != 4:
        if (line3[j] == "O") or (line3[j] == "T"):
            Oc += 1
        j += 1
    j = 0        
    while j != 4:
        if (line4[j] == "O") or (line4[j] == "T"):
            Od += 1
        j += 1
 #Col X
    if (line1[0] == "X") or (line1[0] == "T"):
        Xe += 1
    if (line2[0] == "X") or (line2[0] == "T"):
        Xe += 1
    if (line3[0] == "X") or (line3[0] == "T"):
        Xe += 1
    if (line4[0] == "X") or (line4[0] == "T"):
        Xe += 1
    if (line1[1] == "X") or (line1[1] == "T"):
        Xf += 1
    if (line2[1] == "X") or (line2[1] == "T"):
        Xf += 1
    if (line3[1] == "X") or (line3[1] == "T"):
        Xf += 1
    if (line4[1] == "X") or (line4[1] == "T"):
        Xf += 1        
    if (line1[2] == "X") or (line1[2] == "T"):
        Xg += 1
    if (line2[2] == "X") or (line2[2] == "T"):
        Xg += 1
    if (line3[2] == "X") or (line3[2] == "T"):
        Xg += 1
    if (line4[2] == "X") or (line4[2] == "T"):
        Xg += 1
    if (line1[3] == "X") or (line1[3] == "T"):
        Xh += 1
    if (line2[3] == "X") or (line2[3] == "T"):
        Xh += 1
    if (line3[3] == "X") or (line3[3] == "T"):
        Xh += 1
    if (line4[3] == "X") or (line4[3] == "T"):
        Xh += 1
 
 #Col O
    if (line1[0] == "O") or (line1[0] == "T"):
        Oe += 1
    if (line2[0] == "O") or (line2[0] == "T"):
        Oe += 1
    if (line3[0] == "O") or (line3[0] == "T"):
        Oe += 1
    if (line4[0] == "O") or (line4[0] == "T"):
        Oe += 1
    if (line1[1] == "O") or (line1[1] == "T"):
        Of += 1
    if (line2[1] == "O") or (line2[1] == "T"):
        Of += 1
    if (line3[1] == "O") or (line3[1] == "T"):
        Of += 1
    if (line4[1] == "O") or (line4[1] == "T"):
        Of += 1        
    if (line1[2] == "O") or (line1[2] == "T"):
        Og += 1
    if (line2[2] == "O") or (line2[2] == "T"):
        Og += 1
    if (line3[2] == "O") or (line3[2] == "T"):
        Og += 1
    if (line4[2] == "O") or (line4[2] == "T"):
        Og += 1
    if (line1[3] == "O") or (line1[3] == "T"):
        Oh += 1
    if (line2[3] == "O") or (line2[3] == "T"):
        Oh += 1
    if (line3[3] == "O") or (line3[3] == "T"):
        Oh += 1
    if (line4[3] == "O") or (line4[3] == "T"):
        Oh += 1

#Diag X
    if (line1[0] == "X") or (line1[0] == "T"):
        XD1 += 1        
    if (line2[1] == "X") or (line2[1] == "T"):
        XD1 += 1        
    if (line3[2] == "X") or (line3[2] == "T"):
        XD1 += 1        
    if (line4[3] == "X") or (line4[3] == "T"):
        XD1 += 1        
    
    if (line1[3] == "X") or (line1[3] == "T"):
        XD2 += 1        
    if (line2[2] == "X") or (line2[2] == "T"):
        XD2 += 1        
    if (line3[1] == "X") or (line3[1] == "T"):
        XD2 += 1        
    if (line4[0] == "X") or (line4[0] == "T"):
        XD2 += 1        

#Diag O
    if (line1[0] == "O") or (line1[0] == "T"):
        OD1 += 1        
    if (line2[1] == "O") or (line2[1] == "T"):
        OD1 += 1        
    if (line3[2] == "O") or (line3[2] == "T"):
        OD1 += 1        
    if (line4[3] == "O") or (line4[3] == "T"):
        OD1 += 1        
    
    if (line1[3] == "O") or (line1[3] == "T"):
        OD2 += 1        
    if (line2[2] == "O") or (line2[2] == "T"):
        OD2 += 1        
    if (line3[1] == "O") or (line3[1] == "T"):
        OD2 += 1        
    if (line4[0] == "O") or (line4[0] == "T"):
        OD2 += 1        

#Recherche de .
    pt=0
    j = 0
    while j != 4:
        if (line1[j] == "."):
            pt=1
        j += 1
    j = 0
    while j != 4:
        if (line2[j] == "."):
            pt=1
        j += 1
    j = 0        
    while j != 4:
        if (line3[j] == "."):
            pt=1
        j += 1
    j = 0        
    while j != 4:
        if (line4[j] == "."):
            pt=1
        j += 1
 
    
#    print "mon X (a,b,c,d)", Xa, Xb, Xc, Xd
#    print "mon O (a,b,c,d)", Oa, Ob, Oc, Od
#    print "mon X (e,f,g,h)", Xe ,Xf ,Xg ,Xh
#    print "mon O (e,f,g,h)", Oe ,Of ,Og ,Oh
#    print "mon XD (1,2)", XD1, XD2
#    print "mon OD (1,2)", OD1, OD2
    
#    print line1
#        print "Case #1: X won"
#    print line2

#    print line3

#    print line4
    lineempty=fichier.readline().rstrip('\n\r')

    termX=0
    termO=0
    complete=0
    if (Xa) == 4:
        termX=1
    if (Xb) == 4:
        termX=1
    if (Xc) == 4:
        termX=1
    if (Xd) == 4:
        termX=1
    if (Xe) == 4:
        termX=1
    if (Xf) == 4:
        termX=1
    if (Xg) == 4:
        termX=1        
    if (Xh) == 4:
        termX=1
    if (XD1) == 4:
        termX=1
    if (XD2) == 4:
        termX=1
    if termX == 1:
        print "Case #%i: X won" % tour
    if (OD1) == 4:
        termO=1
    if (OD2) == 4:
        termO=1
    if (Oa) == 4:
        termO=1
    if (Ob) == 4:
        termO=1
    if (Oc) == 4:
        termO=1
    if (Od) == 4:
        termO=1
    if (Oe) == 4:
        termO=1
    if (Of) == 4:
        termO=1
    if (Og) == 4:
        termO=1
    if (Oh) == 4:
        termO=1                        
    if termO == 1:
        print "Case #%i: O won" % tour
    if (termX == 0):
        if (termO == 0):
            if (pt==1):
                print "Case #%i: Game has not completed" % tour   
    if (termX == 0): 
        if (termO == 0):
            if(pt==0):
                print "Case #%i: Draw" % tour
    
#    print lineempty

fichier = open("/tmp/large1","r")

nbtables = fichier.readline().rstrip('\n\r')
nbtables = int(nbtables)
#print nbtables

i = 0

while nbtables != i:
    readtable(i)
    i += 1


fichier.close()