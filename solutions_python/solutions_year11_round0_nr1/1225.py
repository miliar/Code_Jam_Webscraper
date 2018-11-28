#!/bin/python

fin = open("A-large.in","r");
fout = open("out.txt",'w');

T = int(fin.readline());
#print T;
for t  in range(T):
    lsplit = fin.readline().split();
    N = int(lsplit[0]);
    
    PR = lsplit[1:];
    p = [];
    O = [];
    B = [];
    nO = 0;
    nB = 0;
    r= {'O':O,'B':B}
    nr= {'O':-1,'B':-1}
    pos={'O':1,'B':1}
    xR = {'O':'B','B':'O'}
    
    i= 0;
    for n in range(N):
        p.append([PR[2*n],int(PR[2*n+1])]);
        (O if PR[2*n] is 'O' else B ).append(n);
    
#    print p;
    for n in range(N):
        """
        Ada 2 robot
        """
        r_aktif = p[n][0]
        r_na = xR[r_aktif]
        j = abs(p[n][1]-pos[r_aktif])+1
        try :
            xJ = p[r[r_na][nr[r_na]+1]][1]-pos[r_na]
        except IndexError:
            xj=0
        i+=j
        pos[r_aktif] = p[n][1]
        nr[r_aktif]+=1
        #print abs(xJ),j
        if abs(xJ) <= j :
            try :
                pos[r_na] = p[r[r_na][nr[r_na]+1]][1]
                
            except IndexError:
                i
        else :
            #print xJ
            if xJ < 0: pos[r_na]-=(j)
            else : pos[r_na] += (j)
        #print pos
    fout.write("Case #%i: %i\n"%(t+1, i))
    