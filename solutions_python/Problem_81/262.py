import sys
from collections import defaultdict

#sys.stdin = open("in.txt")
sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\A-large.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())

for i in range(1,t+1):
    win = []
    los = []
    l = []
    n = int(raw_input())
    for j in range(n):
        l.append(raw_input())

    wp = []
    for j in range(n):
        wp.append(0.0)
        win.append(0.0)
        los.append(0.0)
        won = 0.0
        lost = 0.0
        for ch in l[j]:
            if ch == '1':
                won+=1.0
                win[j]+=1.0
            elif ch == '0':
                lost+=1.0
                los[j]+=1.0
        if (won + lost) > 0.0: 
            wp[j]=won/(won+lost)
        else:
            wp[j]=0
    
    owp = []
    for j in range(n):
        owp.append(0.0)
        for k in range(n):
            if l[j][k] == '1' or l[j][k] == '0':
                if l[k][j] == '1':
                    if (win[k]+los[k]-1.0)>0.0:
                        owp[j]+=( win[k]-1.0 )/(win[k]+los[k]-1.0)
                    else:
                        owp[j]+=0.0
                else:
                    if (win[k]+los[k]-1.0)>0.0:
                        owp[j]+=( win[k] )/(win[k]+los[k]-1.0)
                    else:
                        owp[j]+=0.0
        if( win[j]+los[j] )>0:
            owp[j] /= ( win[j]+los[j] )
        else:
            owp[j] = 0.0

    oowp = []
    for j in range(n):
        oowp.append(0.0)
        for k in range(n):
            if l[j][k] == '1' or l[j][k]=='0':
                oowp[j] += owp[k]
        if( win[j]+los[j] )>0:
            oowp[j] /= ( win[j] + los[j] )
        else:
            oowp[j] = 0.0
    
    rpi = []
    for j in range(n):
        rpi.append(0.0)
        rpi[j] =  0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]

    print "Case #"+str(i)+":"
    for j in range(n):
        print rpi[j]